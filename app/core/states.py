from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.settings.states import InvoiceForm
from app.api.request_api import request_aurapay_api

router = Router()


@router.message(InvoiceForm.id)
async def invoice_id(message: Message, state: FSMContext):
    await message.answer("ща будет крутой пиздец")

    answer = await request_aurapay_api(message.text)
    await message.answer(answer)

    await state.clear()
