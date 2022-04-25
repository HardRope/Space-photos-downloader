import os
import time

import telegram
from dotenv import load_dotenv

def take_files():
    path = os.getcwd() + r"\image\\"
    tree = os.walk(path)
    images = []
    for address, dirs, files in tree:
        for name in files:
            images.append(os.path.join(address, name))
    return images


if __name__ == '__main__':
    load_dotenv()

    TG_TOKEN = os.getenv('TG-TOKEN')
    bot = telegram.Bot(token=TG_TOKEN)
    channel_id = '@HR_Space_img'

    images_paths = take_files()
    TIME_DELAY = int(os.getenv('TIME-DELAY', default=86400))

    while True:
        for image in images_paths:
            bot.send_document(chat_id=channel_id, document=open(image, "rb"))
            time.sleep(TIME_DELAY)
