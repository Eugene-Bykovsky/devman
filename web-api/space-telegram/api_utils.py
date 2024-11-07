from os.path import splitext
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


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
    Path(directory_name).mkdir(parents=True, exist_ok=True)
