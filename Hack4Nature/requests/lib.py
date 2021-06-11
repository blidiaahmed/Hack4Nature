from dotenv import load_dotenv
import os
load_dotenv()

from Hack4Nature.coordinates_generator.lib import generate_coordinates_in_city
from Hack4Nature.requests.bing.lib import request_image as bing_request_image
from Hack4Nature.requests.google_maps.lib import request_image as google_maps_request_image

from Hack4Nature.storage.local.lib import save_image, delete_image
from Hack4Nature.storage.google_cloud.lib import upload_to_gcp

def generate_local_file(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city, services, destination):
	positions = generate_coordinates_in_city(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city)
	print(positions)
	for service in services:
		for position in positions:
			lat = position[0]
			lon = position[1]
			image = request_image_from_service(lat,lon,service)
			filename = f"raw_data/{service}/{destination}_{lat}_{lon}.png"
			save_image(filename, image)
			print('Going for next position')
		print('Going for next service')
	print('Ended local generation')
	return True

def generate_storage_file(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city, services, destination):
	# a partir de coordonnées et de params, genere un fichier en ligne
	positions = generate_coordinates_in_city(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city)
	for service in services:
		for position in positions:
			lat = position[0]
			lon = position[1]
			image = request_image_from_service(lat,lon,service)
			local_filename = f"raw_data/{service}/{destination}_{lat}_{lon}.png"
			filename = f"{service}/{destination}_{lat}_{lon}.png"
			save_image(local_filename, image)
			upload_to_gcp(filename, service)
			delete_image(local_filename)
			print('Going for next position')
		print('Going for next service')
	print('Ended online generation')
	return True

def request_image_from_service(lat,lon,service):
	if service == "bing":
		params = set_bing_params()
		centerPoint = f"{lat},{lon}"
		image = bing_request_image(centerPoint, params)
	elif service == "google_maps":
		params = set_google_maps_params(lat,lon)
		image = google_maps_request_image(params)
	return image

def set_bing_params():
	format_type = 'png'
	mapSize = '640,640'
	zoomLevel = 20
	key = os.environ.get("BING_MAP_API_KEY")
	params = f"format={format_type}&mapSize={mapSize}&zoomLevel={zoomLevel}&key={key}"
	return params

def set_google_maps_params(lat,lon):
	params = {
		'center': f"{lat},{lon}",
		'zoom':20,
		'size': (640,640),
		'scale':2,
		'maptype': 'satellite'
	}
	return params

# Essai en local pour tester les nouvelles fonctions.
# Départ au dessus de David : 43.2664, 5.3671
# Fin au rond point de Bonneveine : 43.2545, 5.3819
#generate_local_file(43.2545, 5.3671, 43.2664, 5.3819, 0.1, 0.01, "Marseille", ["google_maps", "bing"], "labels")
generate_storage_file(43.2545, 5.3671, 43.2664, 5.3819, 0.1, 0.01, "Marseille", ["google_maps", "bing"], "labels")