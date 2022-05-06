import os
import requests
from pathlib import Path

from urllib.parse import urlparse

def create_directory(user_dir=None, main_dir ='image'):
    if not user_dir:
        file_path = Path.cwd() / main_dir
    else:
        file_path = Path.cwd() / main_dir / user_dir

    Path.mkdir(file_path, parents=True, exist_ok=True)

    return file_path

def get_extension(url):
    path = urlparse(url).path
    file_name = os.path.split(path)[1]
    extension = os.path.splitext(file_name)[1]
    return extension


def download_image(url, path):
    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def load_images(image_list, save_path):

    image_links = image_list

    for num, link in enumerate(image_links, start=1):
        image_extension = get_extension(link)
        image_name = Path(save_path).stem + '-' + str(num) + image_extension
        image_file = save_path / image_name

        download_image(link, image_file)
