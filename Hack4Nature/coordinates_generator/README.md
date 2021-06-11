# Générateur de coordonnées

## Limites des communes

Les limites des communes française peuvent être trouvées ici : https://www.data.gouv.fr/fr/datasets/decoupage-administratif-communal-francais-issu-d-openstreetmap/
Le découpage administratif est donné en longitude, latitude.

La fonction ```coordinates_in_city ``` permet de savoir si les coordonées d'un point appartiennent à une ville présente dans le découpage donné. Elle nécessite des coordonées en latitude, longitude et d'un nom de ville.

## Génération d'une grille de point

La fonction ``` generate_square_coordinates ``` permet de générer à partir des coordonnées de 2 points représentant un carré et d'un pas pour les latitudes et d'un pas pour les longitudes un ensemble de points

## Génération d'une grille de point dans une ville

La fonction ``` generate_coordinates_in_city ``` combine les 2 fonctions précédentes pour éliminer les points non présents dans la zone administrative de la ville donnée en paramètre. 

## Données utilisées et remarques 

Coordonnées de Marseille
En bas => 43.197224 (arrondi à 43.2)
En haut => 43.391017 (arrondi à 43.4)
A gauche => 5.278058 (arrondi à 5.28)
A droite => 5.532462 (arrondi à 5.54)

Code utilisé pour générer les images de training.
Départ de Castellane : 43.2863, 5.3829
lat = 43.2863
lon = 5.3829
pas_lat = 0.0006
pas_lon = 0.0008