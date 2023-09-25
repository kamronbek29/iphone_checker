from constants import ADMINS_ID
from main import bot


# Function to send waiting message
async def send_message(chat_id, msg_to_send, off_notification=True):
    try:
        sent_message = await bot.send_message(chat_id, msg_to_send, disable_notification=off_notification, disable_web_page_preview=True)
        return sent_message
    except Exception as err:
        print(err, 'send_message')
        return False


# Send notification that bot started working
async def on_startup(args):
    for admin_id in ADMINS_ID:
        await send_message(admin_id, 'Бот запущен')
