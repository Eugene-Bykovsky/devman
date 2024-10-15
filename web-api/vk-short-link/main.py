import os
import requests

from dotenv import load_dotenv

load_dotenv()

VK_API_URL = 'https://api.vk.ru/method/'
VK_API_METHODS = {
    'getShortLink': 'utils.getShortLink',
}
TOKEN = os.getenv('SERVICE_TOKEN')


def shorten_link(token, url):
    response = requests.get(
        f'{VK_API_URL+VK_API_METHODS["getShortLink"]}?access_token={token}&v=5'
        f'.199&url={url}')
    response.raise_for_status()
    if 'error' in response.json():
        err_code = response.json()['error']['error_code']
        err_msg = response.json()['error']['error_msg']
        raise ValueError(f'code {err_code} - {err_msg}')
    return response.json()['response']['short_url']


if __name__ == '__main__':
    long_url = input('Введите ссылку: ')
    try:
        print('Сокращенная ссылка: ', shorten_link(TOKEN, long_url))
    except requests.exceptions.HTTPError as http_err:
        print(f"Can't get data from server.HTTP error:\n{http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Can't get data from server. Request error:\n {req_err}")
    except ValueError as api_err:
        print(f'VK API error: {api_err}')


# https://dvmn.org/modules
