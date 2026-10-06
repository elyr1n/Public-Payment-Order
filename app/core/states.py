from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.settings.states import InvoiceForm
from app.url.get_payment_link import get_payment_link

router = Router()


@router.message(InvoiceForm.id)
async def invoice_id(message: Message, state: FSMContext):
    await message.answer("ща будет крутой пиздец")

    answer = await get_payment_link(message.text)
    await message.answer(answer)

    await state.clear()
