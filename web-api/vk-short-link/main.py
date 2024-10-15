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
    return response.json()['response']['short_url']


if __name__ == '__main__':
    long_url = input('Введите ссылку: ')
    print('Сокращенная ссылка: ', shorten_link(TOKEN, long_url))

# https://dvmn.org/modules
