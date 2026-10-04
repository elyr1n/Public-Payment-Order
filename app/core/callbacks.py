import os

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.settings.states import SettingsForm

router = Router()


@router.callback_query(F.data == "settings")
async def settings(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    if int(os.getenv("ADMINS")) != callback.from_user.id:
        return await callback.message.edit_text(
            "леее пошел нахуй ты не можешь ботом пользоваться"
        )

    await state.set_state(SettingsForm.csrf)

    await callback.message.edit_text("напиши свой CSRF, ДЕБИЛ!!!")


@router.callback_query(F.data == "get_link_qr")
async def settings(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    await state.set_state(SettingsForm.data)

    if int(os.getenv("ADMINS")) != callback.from_user.id:
        return await callback.message.edit_text(
            "леее пошел нахуй ты не можешь ботом пользоваться"
        )

    await callback.message.edit_text("а ну напиши данные для запроса")
