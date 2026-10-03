from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.settings.states import SettingsForm
from app.settings.config import neccesary_data

router = Router()


@router.message(SettingsForm.csrf)
async def settings_csrf(message: Message, state: FSMContext):
    await state.update_data(csrf=message.text)
    await state.set_state(SettingsForm.phpsessid)

    await message.answer("теперь дебил настрой PHPSESSID")


@router.message(SettingsForm.phpsessid)
async def settings_phpsessid(message: Message, state: FSMContext):
    await state.update_data(phpsessid=message.text)
    await state.set_state(SettingsForm.golden_key)

    await message.answer("теперь дебил настрой золотой ключ ебать")


@router.message(SettingsForm.golden_key)
async def settings_golden_key(message: Message, state: FSMContext):
    await state.update_data(golden_key=message.text)

    neccesary_data = await state.get_data()

    await message.answer(
        "на дебил смотри че у тебя:\n"
        f"1. сиэсэрэф: {neccesary_data["csrf"]}\n"
        f"2. пхпсессид: {neccesary_data["phpsessid"]}\n"
        f"3. золотой ключик: {neccesary_data["golden_key"]}"
    )
    
    await state.clear()
