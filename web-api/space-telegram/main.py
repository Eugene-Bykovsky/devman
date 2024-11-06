import os
from os.path import splitext
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests
from dotenv import load_dotenv

load_dotenv()


def get_response(url, params=None):
    response = requests.get(url, params)
    response.raise_for_status()
    return response


def download_image(url, save_path):
    response = get_response(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)


def get_file_extension(url):
    url = urlsplit(url)
    _, extension = splitext(unquote(url.path))
    return extension


def make_directory(directory_name):
    Path(f'{directory_name}').mkdir(parents=True, exist_ok=True)


def fetch_spacex_last_launch():
    response = get_response('https://api.spacexdata.com/v5/launches'
                            '/5eb87d47ffd86e000604b38a')
    data = response.json()
    directory_name = 'spacex_launch_photos'
    make_directory(directory_name)
    url_photos = data.get('links', {}).get('flickr', {}).get('original', [])
    for i, url_photo in enumerate(url_photos):
        download_image(url_photo, f'{directory_name}/spacex_{i}.jpg')


def fetch_apod_pictures():
    params = {
        'api_key': os.environ['APOD_NASA_API_KEY'],
        'count': 30
    }
    response = get_response('https://api.nasa.gov/planetary/apod', params)
    data = response.json()
    directory_name = 'apod_pictures'
    make_directory(directory_name)
    url_pictures = [item['url'] for item in data]
    for i, url in enumerate(url_pictures):
        download_image(url, f'{directory_name}/apod_{i}.jpg')


def fetch_epic_pictures():
    params = {
        'api_key': os.environ['EPIC_NASA_API_KEY'],
    }
    response = get_response('https://api.nasa.gov/EPIC/api/natural/images',
                            params)
    photo_data = [(item['image'], item['date'].split()[0].replace('-', '/'))
                  for item in response.json()]
    directory_name = 'epic_pictures'
    make_directory(directory_name)
    for i, item in enumerate(photo_data):
        download_image(f'https://api.nasa.gov/EPIC/archive/natural/{item[1]}/'
                       f'png/{item[0]}.png?api_key'
                       f'=AV1IbpA1Xa9WG7yL0svwZUBIjr8bnm6O87Ni7iDW',
                       f'{directory_name}/epic_{i}.jpg')


def main():
    fetch_spacex_last_launch()
    fetch_apod_pictures()
    fetch_epic_pictures()


if __name__ == '__main__':
    main()
