import os
import datetime

import requests
from dotenv import load_dotenv

from image_loader import *


def get_date(date):
    datetime_format = datetime.datetime.fromisoformat(date)
    format_date = datetime_format.strftime('%Y/%m/%d')
    return format_date


def request_nasa_list(token):
    links_count = 5

    url = f'https://api.nasa.gov/planetary/apod?api_key={token}&count={links_count}'

    response = requests.get(url)
    response.raise_for_status()

    apod_info = response.json()
    image_links = []

    for i in apod_info:
        image_links.append(i['url'])

    return image_links


def request_nasa_epic_list(token):
    api_params= {'api_key': token}
    url = f'https://api.nasa.gov/EPIC/api/natural'

    response = requests.get(url, params=api_params)
    response.raise_for_status()

    epic_list = response.json()
    image_list = []
    for image_info in epic_list:
        image_id = image_info['image']
        date = get_date(image_info['date'])

        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_id}.png%3Fapi_key={token}'
        image_list.append(epic_url)

    return image_list


if __name__ == '__main__':
    load_dotenv()

    nasa_token = os.getenv('NASA-API')

    loading_data = {
        'NASA': request_nasa_list(nasa_token),
        'NASA-Epic': request_nasa_epic_list(nasa_token),
        }

    for name, links in loading_data.items():
        save_path = create_directory(name)
        load_image(links, save_path)
