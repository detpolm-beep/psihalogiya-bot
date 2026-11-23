"""Bot ma'lumotlar bazasi (SQLite).

Foydalanuvchilar va o'tkazilgan testlar natijalarini saqlaydi.
Admin panel statistikasi ham shu yerdan olinadi.
"""

from typing import Optional

import aiosqlite

DB_PATH = "bot.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    user_id     INTEGER PRIMARY KEY,
    username   TEXT,
    first_name TEXT,
    joined_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS test_results (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id   INTEGER NOT NULL,
    test_id   TEXT NOT NULL,
    score     INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_results_user ON test_results(user_id);
CREATE INDEX IF NOT EXISTS idx_results_test ON test_results(test_id);
"""

_conn: Optional[aiosqlite.Connection] = None


async def init_db() -> None:
    """Bazaga ulanish va jadvallarni yaratish (start'da chaqiriladi)."""
    global _conn
    _conn = await aiosqlite.connect(DB_PATH)
    await _conn.executescript(SCHEMA)
    await _conn.commit()


async def close_db() -> None:
    """Bazani yopish (shutdown'da chaqiriladi)."""
    global _conn
    if _conn is not None:
        await _conn.close()
        _conn = None


async def add_user(user_id: int, username: Optional[str],
                   first_name: Optional[str]) -> None:
    """Yangi foydalanuvchini qo'shadi yoki mavjudinini yangilaydi (UPSERT)."""
    await _conn.execute(
        """
        INSERT INTO users (user_id, username, first_name)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            username    = excluded.username,
            first_name  = excluded.first_name,
            last_active = CURRENT_TIMESTAMP
        """,
        (user_id, username, first_name),
    )
    await _conn.commit()


async def log_test_result(user_id: int, test_id: str, score: int) -> None:
    """Yakunlangan test natijasini yozib qo'yadi."""
    await _conn.execute(
        "INSERT INTO test_results (user_id, test_id, score) VALUES (?, ?, ?)",
        (user_id, test_id, score),
    )
    await _conn.commit()


async def get_stats() -> dict:
    """Umumiy statistikani qaytaradi."""
    cur = await _conn.execute("SELECT COUNT(*) FROM users")
    total_users = (await cur.fetchone())[0]

    cur = await _conn.execute("SELECT COUNT(*) FROM test_results")
    total_tests = (await cur.fetchone())[0]

    cur = await _conn.execute(
        "SELECT test_id, COUNT(*) FROM test_results GROUP BY test_id"
    )
    per_test = {row[0]: row[1] for row in await cur.fetchall()}

    cur = await _conn.execute(
        "SELECT COUNT(*) FROM test_results WHERE DATE(created_at)=DATE('now')"
    )
    today_tests = (await cur.fetchone())[0]

    cur = await _conn.execute(
        "SELECT COUNT(*) FROM test_results WHERE created_at >= DATE('now','-6 days')"
    )
    last_7d_tests = (await cur.fetchone())[0]

    return {
        "total_users": total_users,
        "total_tests": total_tests,
        "per_test": per_test,
        "today_tests": today_tests,
        "last_7d_tests": last_7d_tests,
    }


async def get_recent_users(limit: int = 10) -> list:
    """Eng so'nggi foydalanuvchilarni qaytaradi."""
    cur = await _conn.execute(
        "SELECT user_id, username, first_name, joined_at "
        "FROM users ORDER BY joined_at DESC LIMIT ?",
        (limit,),
    )
    return await cur.fetchall()


async def get_all_user_ids() -> list:
    """Broadcast uchun barcha foydalanuvchi ID'lari."""
    cur = await _conn.execute("SELECT user_id FROM users")
    rows = await cur.fetchall()
    return [r[0] for r in rows]
