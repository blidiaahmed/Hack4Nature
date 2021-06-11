# from dotenv import load_dotenv
# import os
# load_dotenv()

from Hack4Nature.coordinates_generator.lib import generate_coordinates_in_city
from Hack4Nature.requests.bing.lib import request_image as bing_request_image
from Hack4Nature.requests.google_maps.lib import request_image as google_maps_request_image

from Hack4Nature.storage.local.lib import save_image, delete_image
from Hack4Nature.storage.google_storage.lib import upload_to_gcp

def generate_local_file(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city, services, destination):
	positions = generate_coordinates_in_city(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city)
	for service in services:
		for position in positions:
			image = request_image_from_service(position[0],position[1],service)
			filename = f"raw_data/{service}/{destination}_{lat}_{lon}.png"
			save_image(filename, image)
			print('Going for next position')
		print('Going for next service')
	print('Ended local generation')
	return True

def generate_storage_file(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city, services):
	# a partir de coordonnées et de params, genere un fichier en ligne
	positions = generate_coordinates_in_city(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon, city)
	for service in services:
		for position in positions:
			image = request_image_from_service(position[0],position[1],service)
			filename = f"{service}/{destination}_{lat}_{lon}.png"
			save_image(filename, image)
			upload_to_gcp(filename)
			delete_image(filename)
			print('Going for next position')
		print('Going for next service')
	print('Ended local generation')
	return True

def request_image_from_service(lat,lon,service):
	if service == "bing":
		params = set_bing_params()
		centerPoint = f"{lat},{lon}"
		image = bing_request_image(centerPoint, params)
	elif service == "google_maps":
		params = set_google_maps_params()
		image = google_maps_request_image(params)
	return image

def set_bing_params():
	format_type = 'png'
	mapSize = '640,640'
	zoomLevel = 20
	key = os.environ.get("BING_MAP_API_KEY")
	params = f"format={format_type}&mapSize={mapSize}&zoomLevel={zoomLevel}&key={key}"
	return params

def set_google_maps_params():
	params = {
		'center': f"{lat},{lon}",
		'zoom':20,
		'size': (2560,2560),
		'scale':2,
		'maptype': 'satellite'
	}
	return params


# def generate_marseille_images(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon):
# 	positions = generate_square_coordinates(start_lat, start_lon, end_lat, end_lon, pas_lat, pas_lon)
# 	for position in positions:
# 		lat = position[0]
# 		lon = position[1]
# 		params = {'center': f"{lat},{lon}",
# 				  'zoom':20,
# 				  'size': (2560,2560),
# 				  'scale':2,
# 				  'maptype': 'satellite'}
# 		save_image(f"labels_{lat_pos}_{lon_pos}.png", params)
# 		upload_to_gcp(f"labels_{lat_pos}_{lon_pos}.png")
# 		delete_image(f"raw_data/labels_{lat_pos}_{lon_pos}.png")
