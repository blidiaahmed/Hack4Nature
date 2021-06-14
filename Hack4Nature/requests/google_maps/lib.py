import googlemaps
from dotenv import load_dotenv
import os
load_dotenv()

def generate_maps_client():
	static_map_api_key = os.environ.get("STATIC_MAP_API_KEY")
	gmaps = googlemaps.Client(key=static_map_api_key)
	return gmaps

def request_image(params):
	gmaps = generate_maps_client()
	image = gmaps.static_map(size=params['size'], zoom=params['zoom'],
							 center=params['center'], scale=params['scale'], 
							 maptype=params['maptype'])
	return image