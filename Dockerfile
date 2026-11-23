# Psixologiya test boti — Docker image (long-polling rejimida ishlaydi)
FROM python:3.11-slim

WORKDIR /app

# Kutubxonalarni alohida o'rnatamiz (Docker layer cache samaradorligi uchun)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini nusxalaymiz
COPY . .

# Muhit o'zgaruvchilari (.env emas, platforma orqali beriladi):
#   BOT_TOKEN  — @BotFather tokeni
#   ADMIN_IDS  — admin telegram ID'lari (vergul bilan)
ENV PYTHONUNBUFFERED=1

# Long-polling jarayonini ishga tushiramiz
CMD ["python", "bot.py"]
