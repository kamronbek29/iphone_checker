import asyncio
import requests

from constants import AVAILABLE_15_PRO_MODELS_URL, PRO_PHONES, STORES_NAME
from helpers import send_message


async def check_phone_availability():
    get_request = requests.get(AVAILABLE_15_PRO_MODELS_URL)
    try:
        get_request_json = get_request.json()
        stores = get_request_json['stores']
    except Exception as err:
        return str(err)

    list_available_phones = []
    for store_id in stores:
        store_phones = stores[store_id]

        for phone_id in store_phones:
            store_phone_model = '{0} - {1}'.format(PRO_PHONES[phone_id], STORES_NAME[store_id])
            phone_info = store_phones[phone_id]
            is_unlocked = phone_info['availability']['unlocked']
            if is_unlocked:
                list_available_phones.append(store_phone_model)

    return list_available_phones


async def start_checking_phones(chat_id):
    for i in range(999999999999):
        await asyncio.sleep(15)

        list_available_phones = await check_phone_availability()

        if list_available_phones == str:
            msg_to_send = f'#{i} - Какая то ошибка: {list_available_phones}'
            await send_message(chat_id, msg_to_send)
            continue

        if not list_available_phones:
            msg_to_send = f'#{i} - Нет доступных телефонов для покупки'
            await send_message(chat_id, msg_to_send)
        else:
            available_phones = '\n'.join(list_available_phones)
            msg_to_send = f'#{i} Есть доступные телефоны для покупки:\n\n{available_phones}\n\n' \
                          f'Ссылка: {AVAILABLE_15_PRO_MODELS_URL}'
            await send_message(chat_id, msg_to_send)
