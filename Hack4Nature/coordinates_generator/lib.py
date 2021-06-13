from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon
import itertools
import numpy as np
import json

def coordinates_in_city(lat,lon,city="Marseille"):
	# Les coordonnées sont en (lat,lon) mais les limites trouvées sont en (lon,lat)
	point = Point(lon,lat)
	with open('Hack4Nature/data/limit_marseille.json') as json_file:
		data = json.load(json_file)
		city_limits = list(filter(lambda feature: feature['properties']['nom'] == city, data['features']))
	data_polygons = city_limits[0]["geometry"]['coordinates']
	polygons = []
	for data_polygon in data_polygons:
		polygon = Polygon(data_polygon[0])
		polygons.append(polygon)
	multipolygon = MultiPolygon(polygons)
	return multipolygon.contains(point)

def generate_square_coordinates(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon):
	lat_pts = np.arange(start_lat, end_lat, pas_lat).tolist()
	lon_pts = np.arange(start_lon, end_lon, pas_lon).tolist()
	all_coordinates = np.array(list(itertools.product(lat_pts, lon_pts)))
	return all_coordinates

def generate_coordinates_in_city(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city="Marseille"):
	all_coordinates = generate_square_coordinates(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon)
	in_city_coordinates = [x for x in all_coordinates if coordinates_in_city(x[0],x[1], city)]
	return in_city_coordinates
