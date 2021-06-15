from dotenv import load_dotenv
import os
load_dotenv()

from Hack4Nature.coordinates_generator.lib import generate_coordinates_in_city
from Hack4Nature.requests.bing.lib import request_image as bing_request_image
from Hack4Nature.requests.google_maps.lib import request_image as google_maps_request_image
from Hack4Nature.requests.mapbox.lib import request_image as mapbox_request_image

from Hack4Nature.storage.local.lib import save_image, delete_image
from Hack4Nature.storage.google_cloud.lib import upload_to_gcp

def generate_local_files(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city, services, destination):
	positions = generate_coordinates_in_city(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city)
	positions_count = len(positions)
	for service in services:
		print(f"Starting {service} import")
		for position in positions:
			index = positions.index(position)
			print(f"Importing position : {index + 1} / {positions_count}")
			lat = position[0]
			lon = position[1]
			generate_local_file(lat,lon, service, destination)
	print('Ended local generation')
	return True

def generate_storage_files(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city, services, destination):
	# a partir de coordonnées et de params, genere un fichier en ligne
	positions = generate_coordinates_in_city(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city)
	positions_count = len(positions)
	for service in services:
		print(f"Starting {service} import")
		for position in positions:
			index = positions.index(position)
			print(f"Importing position : {index + 1} / {positions_count}")
			lat = position[0]
			lon = position[1]
			generate_storage_file(lat,lon, service, destination)
	print('Ended online generation')
	return True

def generate_local_file(lat,lon, service, destination='datas'):
	image = request_image_from_service(lat,lon,service)
	local_filename = f"raw_data/{service}/{destination}_{lat}_{lon}_{service}.png"
	filename = f"{service}/{destination}_{lat}_{lon}.png"
	save_image(local_filename, image)

def generate_storage_file(lat,lon, service, destination='datas'):
	image = request_image_from_service(lat,lon,service)
	local_filename = f"raw_data/{service}/{destination}_{lat}_{lon}_{service}.png"
	filename = f"{service}/{destination}_{lat}_{lon}.png"
	save_image(local_filename, image)
	upload_to_gcp(filename, service)
	delete_image(local_filename)

def request_image_from_service(lat,lon,service):
	if service == "bing":
		image = bing_request_image(lat,lon)
	elif service == "google_maps":
		image = google_maps_request_image(lat,lon)
	elif service == "mapbox":
		image = mapbox_request_image(lon,lat)
	return image

# Essai en local pour tester les nouvelles fonctions.
# Départ au dessus de David : 43.2664, 5.3671
# Fin au rond point de Bonneveine : 43.2545, 5.3819
#generate_local_files(43.2545, 5.3671, 43.2664, 5.3819, 0.1, 0.01, "Marseille", ["google_maps", "bing", "mapbox"], "labels")
# generate_storage_files(43.2545, 5.3671, 43.2664, 5.3819, 0.1, 0.01, "Marseille", ["google_maps", "bing"], "labels")

# Requete test
#lat = 43.291301
#lon = 5.376537
# generate_local_file(lat,lon, 'bing')
# generate_local_file(lat,lon, 'google_maps')
#generate_local_file(lat,lon, 'mapbox')