# Source de données
	
## Bing

Bing documentation : https://docs.microsoft.com/en-us/bingmaps/rest-services/imagery/get-a-static-map#template-parameters

Paramètres fixés : \
	=> format_type : Le format choisi est 'png'. \
	=> mapSize : Le format choisi permet d'avoir une cohérence de donnée avec Google Maps '640,640'. \
	=> zoomLevel : Le zoom choisi permet d'avoir une cohérence de donnée avec Google Maps '20'. \
	=> key : La clé est stockée est le fichier .env à la racine du package sous le nom BING_MAP_API_KEY. \
Paramètres non fixés : \
	=> centerPoint : Les coordonées du centre de la carte en lat,lon. \
URL par défaut : https://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial/{centerPoint}?{params}"
La variable "params" est obtenue par concaténation : 
	``` params = f"format={format_type}&mapSize={mapSize}&zoomLevel={zoomLevel}&key={key}" ```

## Google Maps Static

Google Maps Static documentation : https://developers.google.com/maps/documentation/maps-static/start

Paramètres fixés: \
	=> size : La taille de l'image est (640,640). \
	=> zoom : Le zoom choisi est 20. \
	=> scale : Permet d'obtenir une meilleure résolution (image en 1280 * 1280) avec la valeur 2. \
	=> maptype : Le type de carte est satellite. \
	=> key : La clé est stockée est le fichier .env à la racine du package sous le nom STATIC_MAP_API_KEY. \
Paramètres non fixés : \
	=> center : Les coordonées du centre de la carte en lat,lon \
URL par défaut : https://dev.virtualearth.net/REST/v1/Imagery/Map/Aerial/{centerPoint}?{params}"
La variable "params" est obtenue par concaténation : 
	``` params = {'center': f"{lat},{lon}",
				  'zoom':20,
				  'size': (640,640),
				  'scale':2,
				  'maptype': 'satellite'} 
	```

## MAPBOX

Mapbox Static documentation : https://docs.mapbox.com/api/maps/static-images/
Pour tester des requetes : https://docs.mapbox.com/playground/static/
MAPBOX_TOKEN

# Fonctions utilisables

## generate_local_file

Cette fonction génère des images en local. Elle nécessite les paramètres suivants : \
	=> start_lat, latitude la plus haute de la zone à analyser
	=> start_lon, longitude la plus à gauche de la zone à analyser
	=> end_lat, latitude la plus basse de la zone à analyser
	=> end_lon, longitude la plus à gauche de la zone à analyser
	=> pas_lat, espacement entre chaque latitude pour la génération de la grille de points
	=> pas_lon, espacement entre chaque longitude pour la génération de la grille de pointscity
	=> services, les services appelés (google_maps, bing)
	=> destination, le format du fichier (labels, datas)

## generate_storage_file

Cette fonction génère des images et les télécharges sur Google Cloud Storage. Elle nécessite les paramètres suivants : \
	=> start_lat, latitude la plus haute de la zone à analyser
	=> start_lon, longitude la plus à gauche de la zone à analyser
	=> end_lat, latitude la plus basse de la zone à analyser
	=> end_lon, longitude la plus à gauche de la zone à analyser
	=> pas_lat, espacement entre chaque latitude pour la génération de la grille de points
	=> pas_lon, espacement entre chaque longitude pour la génération de la grille de pointscity
	=> services, les services appelés (google_maps, bing)
	=> destination, le format du fichier (labels, datas)
