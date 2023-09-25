import requests

from constants import AVAILABLE_15_PRO_MODELS_URL, PRO_PHONES


async def checker():
    get_request = requests.get(AVAILABLE_15_PRO_MODELS_URL)
    get_request_json = get_request.json()
    stores = get_request_json['stores']

    list_available_phones = []
    for one_store in stores:
        store_phones = stores[one_store]

        for one_phone in store_phones:
            phone_model = PRO_PHONES[one_phone]
            phone_info = store_phones[one_phone]
            is_unlocked = phone_info['availability']['unlocked']
            if is_unlocked:
                list_available_phones.append(phone_model)

    return list_available_phones
