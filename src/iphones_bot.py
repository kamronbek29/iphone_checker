from aiogram.types import Message
from aiogram.utils import executor

from constants import ADMINS_ID
from helpers import on_startup, send_message
from iphones import start_checking_phones
from main import dp


IS_STARTED = False


@dp.message_handler(commands=['start_check'], chat_type='private', chat_id=ADMINS_ID)
async def start_check_command(message: Message):
    chat_id = message.chat.id

    global IS_STARTED
    if not IS_STARTED:
        msg_to_send = 'Вы успешно запустили отправку уведомлений'
        await send_message(chat_id, msg_to_send)
        await start_checking_phones(chat_id)
    else:
        msg_to_send = 'Вы уже запустили отправку уведомлений'
        await send_message(chat_id, msg_to_send)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
