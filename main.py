import datetime
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def check_directory(user_dir=None):
    file_path = os.getcwd() + r"\image\\"
    if user_dir:
        file_path += user_dir + "\\"
    directory = os.path.dirname(file_path)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)


def get_extension(url):
    path = urlparse(url).path
    file_name = os.path.split(path)[1]
    extension = os.path.splitext(file_name)[1]
    return extension


def get_date(date):
    datetime_format = datetime.datetime.fromisoformat(date)
    format_date = datetime_format.strftime('%Y/%m/%d')
    return format_date


def download_image(url, path):
    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def spacex_list_request():
    launch_id = "6161d32d6db1a92bfba85359"
    response = requests.get(
        f"https://api.spacexdata.com/v4/launches/{launch_id}")
    response.raise_for_status()

    image_list = response.json()['links']['flickr']['original']
    return image_list


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


def image_loader(image_list, directory_name=None):
    check_directory(directory_name)

    image_links = image_list
    save_path = os.getcwd() + r"\image\\" + directory_name + "\\"

    for num, link in enumerate(image_links, start=1):
        image_extension = get_extension(link)
        image_name = directory_name + '-' + str(num) + image_extension
        image_file = save_path + image_name

        download_image(link, image_file)


if __name__ == '__main__':
    load_dotenv()
    check_directory()

    loading_data = {
        'NASA': nasa_list_request(),
        'NASA-Epic': nasa_epic_list_request(),
        'SpaceX': spacex_list_request(),
        }

    for name, links in loading_data.items():
        image_loader(links, name)
