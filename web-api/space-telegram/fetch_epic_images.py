import os
from api_utils import get_response, download_image, make_directory
from dotenv import load_dotenv

load_dotenv()


def fetch_epic_images():
    params = {'api_key': os.environ['EPIC_NASA_API_KEY']}
    response = get_response('https://api.nasa.gov/EPIC/api/natural/images',
                            params)
    images_data = [(item['image'], item['date'].split()[0].replace('-', '/'))
                  for item in response.json()]
    directory_name = 'epic_images'
    make_directory(directory_name)
    for i, item in enumerate(images_data):
        download_image(f'https://api.nasa.gov/EPIC/archive/natural/{item[1]}/'
                       f'png/{item[0]}.png?'
                       f'api_key={os.environ["EPIC_NASA_API_KEY"]}',
                       f'{directory_name}/epic_{i}.jpg')


if __name__ == '__main__':
    fetch_epic_images()