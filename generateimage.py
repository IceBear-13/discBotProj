import requests
import settings
import random


def get_random(search : str) -> str:
    search_query = search

    url = 'https://www.googleapis.com/customsearch/v1'

    params = {
        'q': search_query,
        'key' : settings.GOOGLE_API_KEY,
        'cx' : settings.SEARCH_ENGINE_ID,
        'searchType': 'image'
    }

    r = requests.get(url, params=params)
    result = r.json()

    num = random.randint(1, 10)

    if 'items' in result:
        return result['items'][num-1]['link']
    return 'Item not found'
