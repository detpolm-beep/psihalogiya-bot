"""FSM holatlari — foydalanuvchi test topshirayotganini kuzatish uchun."""

from aiogram.fsm.state import State, StatesGroup


class TestingStates(StatesGroup):
    # Foydalanuvchi test savollariga javob berish jarayonida
    in_test = State()


class AdminStates(StatesGroup):
    # Admin broadcast xabarini kiritishni kutish holati
    waiting_broadcast = State()
