import requests
from dotenv import load_dotenv
import os
load_dotenv()

def request_image(lat,lon):
	params = set_params(lat,lon)
	url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/{params}"
	request = requests.get(url)
	if request.status_code == 200:
	    return request
	else:
		print('Error')
		return False

def set_params(lat,lon):
	mapbox_api_key = os.environ.get("MAPBOX_TOKEN")
	zoom = 20
	width = 1280
	height = 1280
	params = f"{lat},{lon},{zoom},0/{width}x{height}?access_token={mapbox_api_key}"
	return params
