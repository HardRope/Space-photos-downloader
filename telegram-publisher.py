import os
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv

def get_paths(dir):
    dirpath = Path.cwd() / dir
    tree = os.walk(dirpath)
    image_paths = []
    for filepaths, dirs, files in tree:
        for filename in files:
            image_paths.append(os.path.join(filepaths, filename))
    return image_paths


if __name__ == '__main__':
    load_dotenv()

    tg_token = os.getenv('TG-TOKEN')
    bot = telegram.Bot(token=tg_token)
    channel_id = os.getenv('CHANNEL-ID')

    image_paths = get_paths('image')
    time_delay = int(os.getenv('TIME-DELAY', default=86400))

    for image in image_paths:
        with open(image, "rb") as photo:
            bot.send_document(chat_id=channel_id, document=photo)
        time.sleep(time_delay)

