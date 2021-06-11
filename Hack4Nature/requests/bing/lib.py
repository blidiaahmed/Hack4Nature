import requests

def request_image(centerPoint, params):
	url = f"https://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial/{centerPoint}?{params}"
	request = requests.get(url)
	if request.status_code == 200:
	    return request
	else:
		print('Error')
		return False