import os

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.settings.states import InvoiceForm

from dotenv import load_dotenv

load_dotenv()

router = Router()

admins = os.getenv("ADMINS").split(", ")


@router.callback_query(F.data == "get_public_link")
async def get_public_link(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    if str(callback.from_user.id) not in admins:
        return await callback.message.edit_text(
            "леее пошел нахуй ты не можешь ботом пользоваться"
        )

    await state.set_state(InvoiceForm.id)
    await callback.message.edit_text(
        "пидорас а ну быстро написал айди счета в формате UUID"
    )
