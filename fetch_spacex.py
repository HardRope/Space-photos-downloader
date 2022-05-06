import os

import requests
from dotenv import load_dotenv

import image_loader as i_loader

def request_spacex_list(id):
    response = requests.get(
        f"https://api.spacexdata.com/v4/launches/{id}")
    response.raise_for_status()

    image_links = response.json()['links']['flickr']['original']
    return image_links


if __name__ == '__main__':
    load_dotenv()

    launch_id = os.getetnv('LAUNCH_-ID')

    load_pack_links = {
        'SpaceX': request_spacex_list(launch_id),
        }

    for name, link in load_pack_links.items():
        save_path = i_loader.create_directory(name)
        i_loader.load_images(link, save_path)
