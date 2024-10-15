import os
import requests

from dotenv import load_dotenv
from urllib.parse import urlparse
from urllib.parse import urldefrag

load_dotenv()

VK_API_URL = 'https://api.vk.ru/method/'
VK_API_METHODS = {
    'getShortLink': 'utils.getShortLink',
    'getLinkStats': 'utils.getLinkStats',
}
TOKEN = os.getenv('SERVICE_TOKEN')


def shorten_link(token, link):
    response = requests.get(
        f'{VK_API_URL+VK_API_METHODS["getShortLink"]}?access_token={token}&v=5'
        f'.199&url={link}')
    response.raise_for_status()
    if 'error' in response.json():
        err_code = response.json()['error']['error_code']
        err_msg = response.json()['error']['error_msg']
        raise ValueError(f'code {err_code} - {err_msg}')
    return response.json()['response']['short_url']


def count_clicks(token, link):
    link = urlparse(link).path.replace('/', '')
    response = requests.get(
        f'{VK_API_URL+VK_API_METHODS["getLinkStats"]}?access_token={token}&v=5'
        f'.199&key={link}&interval=forever')
    response.raise_for_status()
    if 'error' in response.json():
        err_code = response.json()['error']['error_code']
        err_msg = response.json()['error']['error_msg']
        raise ValueError(f'code {err_code} - {err_msg}')
    return response.json()['response']['stats'][0]['views']


if __name__ == '__main__':
    long_link = input('Введите ссылку: ')
    try:
        short_link = shorten_link(TOKEN, long_link)
        count_clicks = count_clicks(TOKEN, short_link)
        print('Сокращенная ссылка: ', short_link)
        print('Количество кликов по ссылке: ', count_clicks)
    except requests.exceptions.HTTPError as http_err:
        print(f"Can't get data from server.HTTP error:\n{http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Can't get data from server. Request error:\n {req_err}")
    except ValueError as api_err:
        print(f'VK API error: {api_err}')


# https://dvmn.org/modules
# https://vk.cc/cvPDMl
