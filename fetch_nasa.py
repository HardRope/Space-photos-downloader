import os
import datetime

import requests
from dotenv import load_dotenv

from image_loader import *


def get_date(date):
    datetime_format = datetime.datetime.fromisoformat(date)
    format_date = datetime_format.strftime('%Y/%m/%d')
    return format_date


def nasa_list_request():
    API = os.getenv('NASA-API')
    links_count = 5
    url = f'https://api.nasa.gov/planetary/apod?api_key={API}&count={links_count}'

    response = requests.get(url)
    response.raise_for_status

    apod_list = response.json()
    image_links = []

    for i in apod_list:
        image_links.append(i['url'])

    return image_links


def nasa_epic_list_request():
    API = os.getenv('NASA-API')
    url = f'https://api.nasa.gov/EPIC/api/natural?api_key={API}'

    response = requests.get(url)
    response.raise_for_status

    epic_list = response.json()
    image_list = []
    for image_info in epic_list:
        image_id = image_info['image']
        date = get_date(image_info['date'])

        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_id}.png?api_key={API}'
        image_list.append(epic_url)

    return image_list


if __name__ == '__main__':
    load_dotenv()
    check_directory()

    loading_data = {
        'NASA': nasa_list_request(),
        'NASA-Epic': nasa_epic_list_request(),
        }

    for name, links in loading_data.items():
        image_loader(links, name)
