import argparse
from api_utils import get_response, download_image, make_directory


def fetch_spacex_images(launch_id):
    response = get_response(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    data = response.json()
    directory_name = 'spacex_launch_images'
    make_directory(directory_name)
    url_images = data.get('links', {}).get('flickr', {}).get('original', [])
    for i, url_image in enumerate(url_images):
        download_image(url_image, f'{directory_name}/spacex_{i}.jpg')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download SpaceX launch '
                                                 'images')
    parser.add_argument('--launch_id', type=str,
                        help='ID of the SpaceX launch')
    args = parser.parse_args()
    fetch_spacex_images(args.launch_id if args.launch_id
                        else 'latest')
