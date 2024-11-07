import os

import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()

    token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    bot = telegram.Bot(token)
    bot.send_message(chat_id, 'Hello')

    photo_path = './apod_images/apod_0.jpg'
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo)


if __name__ == '__main__':
    main()
