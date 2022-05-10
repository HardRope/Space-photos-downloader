import os
import datetime

import requests
from dotenv import load_dotenv

from image_loader import create_directory, load_images

def format_date(date):
    transform_to_datetime = datetime.datetime.fromisoformat(date)
    formatted_date = transform_to_datetime.strftime('%Y/%m/%d')
    return formatted_date


def request_nasa_list(token):
    links_count = 5
    nasa_params = {
        'api_key': token,
        'count': links_count,
        }
    url = f'https://api.nasa.gov/planetary/apod'

    response = requests.get(url, params=nasa_params)
    response.raise_for_status()

    apod_images_specifications = response.json()
    image_links = []

    for image_specification in apod_images_specifications:
        image_links.append(image_specification['url'])

    return image_links


def request_nasa_epic_list(token):
    api_params= {'api_key': token}
    url = f'https://api.nasa.gov/EPIC/api/natural'

    response = requests.get(url, params=api_params)
    response.raise_for_status()

    epic_images_specifications = response.json()
    image_links = []
    for image_specification in epic_images_specifications:
        image_id = image_specification['image']
        date = format_date(image_specification['date'])

        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_id}.png%3Fapi_key={token}'
        image_links.append(epic_url)

    return image_links


if __name__ == '__main__':
    load_dotenv()

    nasa_token = os.getenv('NASA-API')

    load_packs_links = {
        'NASA': request_nasa_list(nasa_token),
        'NASA-Epic': request_nasa_epic_list(nasa_token),
        }

    for name, links in load_packs_links.items():
        save_path = create_directory(name)
        load_images(links, save_path)
