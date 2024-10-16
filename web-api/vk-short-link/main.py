import os
import requests

from dotenv import load_dotenv
from urllib.parse import urlparse

VK_API_URL = 'https://api.vk.ru/method/'
VK_API_METHODS = {
    'getShortLink': 'utils.getShortLink',
    'getLinkStats': 'utils.getLinkStats',
}


def get_link_key(url: str) -> str:
    """Достает из ссылки часть URL после «/»"""
    return urlparse(url).path.replace('/', '')


def vk_api_request(method: str, params: dict) -> dict:
    """Делает запрос в API VK"""
    response = requests.get(f'{VK_API_URL}{VK_API_METHODS[method]}',
                            params=params)
    response.raise_for_status()
    if 'error' in response.json():
        err_code = response.json()['error']['error_code']
        err_msg = response.json()['error']['error_msg']
        raise ValueError(f'Ошибка в методе - {method}. '
                         f'Code {err_code} - {err_msg}')
    return response.json()


def is_shorten_link(token: str, url: str) -> bool:
    """Проверяем, является ли ссылка сокращенной через запрос к API."""
    link_key = get_link_key(url)
    params = {
        'access_token': token,
        'v': '5.199',
        'key': link_key,
        'interval': 'forever'
    }
    try:
        vk_api_request('getLinkStats', params)
        return True
    except ValueError:
        return False


def shorten_link(token: str, url: str) -> str:
    """Преобразует длинную ссылку в короткую с помощью API VK"""
    params = {
        'access_token': token,
        'v': '5.199',
        'url': url
    }
    return vk_api_request('getShortLink', params)['response']['short_url']


def count_clicks(token: str, url: str) -> int:
    """Возвращает количество кликов по ссылке с помощью API VK"""
    link_key = get_link_key(url)
    params = {
        'access_token': token,
        'v': '5.199',
        'key': link_key,
        'interval': 'forever'
    }
    return vk_api_request('getLinkStats', params)['response']['stats'][0][
        'views']


def main():
    load_dotenv()
    try:
        token = os.environ['VK_API_SERVICE_TOKEN']
    except KeyError as key_err:
        print(f'KeyError: {key_err}')
        raise SystemExit

    link = input('Введите ссылку: ')
    try:
        if is_shorten_link(token, link):
            clicks_count = count_clicks(token, link)
            print('Количество кликов по ссылке: ', clicks_count)
        else:
            short_link = shorten_link(token, link)
            print('Сокращенная ссылка: ', short_link)
    except requests.exceptions.HTTPError as http_err:
        print(f"Can't get data from server.HTTP error:\n{http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Can't get data from server. Request error:\n {req_err}")
    except ValueError as api_err:
        print(f'VK API error: {api_err}')


if __name__ == '__main__':
    main()
