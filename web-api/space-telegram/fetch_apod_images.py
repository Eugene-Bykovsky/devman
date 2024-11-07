import os

from dotenv import load_dotenv

from api_utils import download_image, get_response, make_directory


def fetch_apod_images():
    load_dotenv()

    params = {'api_key': os.environ['APOD_NASA_API_KEY'], 'count': 30}
    response = get_response('https://api.nasa.gov/planetary/apod', params)
    data = response.json()
    directory_name = 'apod_images'
    make_directory(directory_name)
    url_images = [item['url'] for item in data]
    for i, url in enumerate(url_images):
        download_image(url, f'{directory_name}/apod_{i}.jpg')


if __name__ == '__main__':
    fetch_apod_images()
