import requests
from dotenv import load_dotenv
import os
load_dotenv()

def request_image(lat,lon):
	url = "https://maps.googleapis.com/maps/api/staticmap"
	params = set_params(lat,lon)
	request = requests.get(url, params=params)
	if request.status_code == 200:
	    return request
	else:
		print('Error')
		return False

def set_params(lat,lon):
	params = {
		'center': f"{lat},{lon}",
		'zoom':20,
		'size': '1280x1280',
		'scale':2,
		'maptype': 'satellite',
		'key': os.environ.get("STATIC_MAP_API_KEY")
	}
	return params