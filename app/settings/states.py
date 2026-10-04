from aiogram.fsm.state import State, StatesGroup


class SettingsForm(StatesGroup):
    csrf = State()
    phpsessid = State()
    golden_key = State()
    data = State()
