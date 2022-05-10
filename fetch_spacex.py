import os

import requests
from dotenv import load_dotenv

from image_loader import create_directory, load_images

def request_spacex_list(launch_id):
    response = requests.get(
        f"https://api.spacexdata.com/v4/launches/{launch_id}")
    response.raise_for_status()

    image_links = response.json()['links']['flickr']['original']
    return image_links


if __name__ == '__main__':
    load_dotenv()

    launch_id = os.getetnv('LAUNCH-ID')

    load_pack_links = {
        'SpaceX': request_spacex_list(launch_id),
        }

    for name, link in load_pack_links.items():
        save_path = create_directory(name)
        load_images(link, save_path)
