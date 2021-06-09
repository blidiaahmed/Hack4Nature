import requests
import matplotlib.pyplot as plt
from PIL import Image






url = "https://maps.googleapis.com/maps/api/staticmap"
params = {'center': '43.3032768,5.4806885',
          'zoom':21,
          'size':'400x400',
          'scale':2,
          'maptype': 'satellite',
          'key': 'Put your API key here'}

def callmap(filename, params):
    url = "https://maps.googleapis.com/maps/api/staticmap"
    req = requests.get(url, params=params)
    if req.status_code == 200:
        file = open(f"raw_data/{filename}", "wb")
        file.write(req.content)
        file.close()
    else:
        print("WARNING")
        print(req.status_code)
        print(req.content)
    image = Image.open(f"raw_data/{filename}")
    image.show()