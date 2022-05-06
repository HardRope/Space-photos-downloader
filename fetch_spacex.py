import os

import requests
from dotenv import load_dotenv

import image_loader as i_loader

def request_spacex_list(id):
    response = requests.get(
        f"https://api.spacexdata.com/v4/launches/{id}")
    response.raise_for_status()

    image_list = response.json()['links']['flickr']['original']
    return image_list


if __name__ == '__main__':
    load_dotenv()

    launch_id = "6161d32d6db1a92bfba85359"

    loading_data = {
        'SpaceX': request_spacex_list(launch_id),
        }

    for name, links in loading_data.items():
        save_path = i_loader.create_directory(name)
        i_loader.load_image(links, save_path)
