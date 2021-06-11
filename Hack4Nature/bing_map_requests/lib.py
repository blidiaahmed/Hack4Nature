from dotenv import load_dotenv
import os
import requests
load_dotenv()

from Hack4Nature.google_cloud_storage.lib import upload_to_gcp

def request_image(centerPoint, params):
	url = f"https://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial/{centerPoint}?{params}"
	request = requests.get(url)
	if request.status_code == 200:
	    return request
	else:
		print('Error')
		return False

def save_image(filename,centerPoint, params):
	image = request_image(centerPoint, params)
	with open(f"raw_data/{filename}", "wb") as fp:
		for chunk in image:
			fp.write(chunk)
	return True

def delete_image(filename):
	os.remove(filename)
	return True

format_type = 'png'
mapSize = '640,640' #permet même zoom que Google
zoomLevel = 20
key = os.environ.get("BING_MAP_API_KEY")
params = f"format={format_type}&mapSize={mapSize}&zoomLevel={zoomLevel}&key={key}"
save_image("bing.png", '43.2863,5.3909', params)
