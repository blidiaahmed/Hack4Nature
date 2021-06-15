import googlemaps
from dotenv import load_dotenv
import os
load_dotenv()

def generate_maps_client():
	static_map_api_key = os.environ.get("STATIC_MAP_API_KEY")
	gmaps = googlemaps.Client(key=static_map_api_key)
	return gmaps

def request_image(lat,lon):
	gmaps = generate_maps_client()
	params = set_params(lat,lon)
	image = gmaps.static_map(size=params['size'], zoom=params['zoom'],
							 center=params['center'], scale=params['scale'], 
							 maptype=params['maptype'])
	return image

def set_params(lat,lon):
	params = {
		'center': f"{lat},{lon}",
		'zoom':20,
		'size': (640,640),
		'scale':2,
		'maptype': 'satellite'
	}
	return params