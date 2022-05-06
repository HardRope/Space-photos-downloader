# Space-to-Telegram

This programm created to download some Space and rocket launches photos from SpaceX and NASA (using NASA API) and publish it to Telegram channel

## How to use

To use script, you need to create `.env` with some tokens:
* `NASA-API='nasa_token_here'`
* `TG-TOKEN='telegramm-bot-token'`
* `CHANNEL-ID='channel link (@ChanellName)'`
* `TIME-DELAY=86400`
* `LAUNCH-ID='lainch_id_here'`

Link to create api-token: [NASA](https://api.nasa.gov/)

Help with obtain TG-Token: [Bot Father](https://telegram.me/BotFather)

Time delay is seconds value between publishing photo to channel. Default value = 86400 sec (1 day), can be changed in `.env`.

After creating `.env` file, run `fetch_nasa` and `fetch_spacex` to download images.

Console command to run:

```
python fetch_nasa.py

python fetch_spacex`.py
```

Launch `Telegram-publisher` create endless cycle, that publish one image per a day to your TG-channel.

```
python Telegram_publisher.py
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```


## Remark

In current version script collect links and download photos from 3 places:
- SpaceX API

	Download photos from selected launch, but you could change choice by changing launch ID in `spacex_list_request()` function at `fetch_spacex`.
	Current `launch_id = '6161d32d6db1a92bfba85359'`
	
- NASA APOD (Astronomy Picture of the Day)

	Collect and download some APOD-photos from histoty, current count = 5,
	to change it - change `links_count` in `nasa_list_request()` function at `fetch_nasa`.
	
- NASA EPIC (Earth Polychromatic Imaging Camera)

	Download some Earth photos made on today's date
	
## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
