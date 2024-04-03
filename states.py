from aiogram.fsm.state import StatesGroup, State

class Application(StatesGroup):
    name = State()
    age = State()
    phone = State()
    job = State()
    goal = State()
