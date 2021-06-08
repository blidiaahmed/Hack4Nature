import googlemaps
from datetime import datetime
from dotenv import load_dotenv
import os

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

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

def export_image(filename, params):
	image = request_image(params)
	with open(f"raw_data/{filename}", "wb") as fp:
	    for chunk in image:
	        fp.write(chunk)
	return True

point = Point(0.5, 0.5)
polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
print(polygon.contains(point))


params = {'center': '43.3032768,5.4800',
		  'zoom':20,
		  'size': (2560,2560),
		  'scale':2,
		  'maptype': 'satellite'}
export_image("lib_export_test.png", params)

params = {'center': '43.3032768,5.4805',
		  'zoom':20,
		  'size': (2560,2560),
		  'scale':2,
		  'maptype': 'satellite'}
export_image("lib_export_test_2.png", params)

# Sur la longitude, un pas de 0.001 est trop grand.
# Sur la longitude, un pas de 0.0005 est trop petit ? 

# En haut => 43.391017 (arrondir à 43.395)
# A gauche => 5.278058 (arrondir à 5.280)
# A droite => 5.532462 (arrondir à 5.535)
# En bas => 43.197224 (arrondir à 43.195)

# nombre de photos hauteur
p_haut = (43.395 - 43.195) / 0.0005
p_bas = (5.535 - 5.28) / 0.0005