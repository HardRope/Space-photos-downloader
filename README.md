# Space photos downloader

This programm created to download some space photos from SpaceX launches and NASA Libraries (using NASA API).

## How to use

To use script, you need to create `.env` file with NASA Token, formate `NASA-API = 'nasa_token_here'`.
Link to create api-token: [NASA](https://api.nasa.gov/)

After launching the programm, it create in your current work directory folder "image" and begin to download photos, sorting them into named folders.

## Remark

In current version script collect links and download photos from 3 places:
- SpaceX API
	Download photos from selected launch, but you could change choice by changing launch ID in `spacex_list_request()` function.
	Current `launch_id = '6161d32d6db1a92bfba85359'`
	
- NASA APOD (Astronomy Picture of the Day)
	Collect and download some APOD-photos from histoty, current count = 5,
	to change it - change `links_count` in `nasa_list_request()` function.
	
- NASA EPIC (Earth Polychromatic Imaging Camera)
	Download some Earth photos made on today's date
