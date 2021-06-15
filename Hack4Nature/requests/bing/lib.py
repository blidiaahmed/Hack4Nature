import requests
from dotenv import load_dotenv
import os
load_dotenv()

def request_image(lat,lon):
	centerPoint = f"{lat},{lon}"
	params = set_params()
	url = f"https://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial/{centerPoint}?{params}"
	
	request = requests.get(url)

	if request.status_code == 200:
	    return request
	else:
		print('Error')
		return False

def set_params():
	format_type = 'png'
	mapSize = '640,640'
	zoomLevel = 20
	key = os.environ.get("BING_MAP_API_KEY")
	params = f"format={format_type}&mapSize={mapSize}&zoomLevel={zoomLevel}&key={key}"
	return params