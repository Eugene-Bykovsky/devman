import os
import requests

from dotenv import load_dotenv

load_dotenv()

URL = 'https://api.vk.ru/method/utils.getServerTime'
TOKEN = os.getenv('SERVICE_TOKEN')
PAYLOAD = {
    'access_token': TOKEN,
    'v': 5.199,
}

response = requests.get(URL, params=PAYLOAD)

if __name__ == '__main__':
    print(response.text)
