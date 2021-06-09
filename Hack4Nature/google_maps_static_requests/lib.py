import googlemaps
from datetime import datetime
from dotenv import load_dotenv
import os
import json
import numpy as np
import itertools

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon

from Hack4Nature.google_cloud_storage.lib import upload_to_gcp
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

def save_image(filename, params):
	image = request_image(params)
	with open(f"raw_data/{filename}", "wb") as fp:
		for chunk in image:
			fp.write(chunk)
	return True

def delete_image(filename):
	os.remove(filename)

def coordinates_in_city(lat,lon):
	point = Point(lon,lat)
	with open('Hack4Nature/data/limit_marseille.json') as json_file:
		data = json.load(json_file)
		data_polygons = data['features'][0]["geometry"]['coordinates']
		polygons = []
		for data_polygon in data_polygons:
			polygon = Polygon(data_polygon[0])
			polygons.append(polygon)
	multipolygon = MultiPolygon(polygons)
	return multipolygon.contains(point)

# WARNING !!!! Les coordonnées sont à donner en (lat,lon) mais les limites sont en (lon,lat)
# coordinates_in_city(43.3032768,5.4800)


def generate_square_coordinates(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon):
	lat_pts = np.arange(start_lat, end_lat, pas_lat).tolist()
	lon_pts = np.arange(start_lon, end_lon, pas_lon).tolist()
	all_coordinates = np.array(list(itertools.product(lat_pts, lon_pts)))
	print(len(all_coordinates))
	# in_marseille_coordinates = list(
	# 	filter(lambda coordinates: coordinates_in_city(coordinates[0],coordinates[1]), all_coordinates))
	in_marseille_coordinates = [x for x in all_coordinates if coordinates_in_city(x[0],x[1])]
	print(len(in_marseille_coordinates))
	return in_marseille_coordinates

# En bas => 43.197224 (arrondir à 43.2)
# En haut => 43.391017 (arrondir à 43.4)
# A gauche => 5.278058 (arrondir à 5.28)
# A droite => 5.532462 (arrondir à 5.54)
generate_square_coordinates(43.20, 5.28, 43.40, 5.54, 0.0006, 0.0008)

def generate_marseille_images(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon):
	positions = generate_square_coordinates(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon)
	for position in positions:
		lat = position[0]
		lon = position[1]
		params = {'center': f"{lat},{lon}",
				  'zoom':20,
				  'size': (2560,2560),
				  'scale':2,
				  'maptype': 'satellite'}
		save_image(f"labels_{lat_pos}_{lon_pos}.png", params)
		upload_to_gcp(f"labels_{lat_pos}_{lon_pos}.png")
		delete_image(f"raw_data/labels_{lat_pos}_{lon_pos}.png")

# Code utilisé pour générer les images de training.
#Départ de Castellane : 43.2863, 5.3829
# lat = 43.2863
# lon = 5.3829
# pas_lat = 0.0006
# pas_lon = 0.0008
# for i in range(10):
# 	for j in range(10):
# 		lat_pos = lat + pas_lat*i
# 		lon_pos = lon + pas_lon*j
# 		params = {'center': f"{lat_pos},{lon_pos}",
# 				  'zoom':20,
# 				  'size': (2560,2560),
# 				  'scale':2,
# 				  'maptype': 'satellite'}
# 		save_image(f"labels_{lat_pos}_{lon_pos}.png", params)
# 		upload_to_gcp(f"labels_{lat_pos}_{lon_pos}.png")
# 		delete_image(f"raw_data/labels_{lat_pos}_{lon_pos}.png")
