from aiogram.fsm.state import State, StatesGroup


class InvoiceForm(StatesGroup):
    id = State()
