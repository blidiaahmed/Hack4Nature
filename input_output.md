# Input_Output de DeepForest

## Input
Deepforest prend en input un fichier csv avec ces colonnes :

image_path	xmin	ymin	xmax	ymax	label

chaque donnée correspond à un cadre qui entoure un arbre de l'image.

image_path : Le chemin pour trouver l'image sur notre disque.

xmin,ymin = les coordonnées du point en bas à gauche du cadre.

xmax,ymax = les coordonnées du point en haut à droite du cadre.

label = tree On utilisera uniquement celui-ci puisqu'on veut predire uniquement des arbres.

## Output
Deepforest possède plusieurs manière de faire des predict une fois notre modèle entrainé :

predict_image pour trouver les arbres sur une image de taille raisonnable
si on lui entre le paramètre return_plot = True, elle renverra directement une image.
Sinon, elle renvoie un dataframe avec les xmin,ymin,xmax,	ymax de chacun des cadres, ainsi qu'un score.
Je suppose que le score correspond à la certitude qu'a l'algorithme qu'il a bien encadré un arbre.

Il y a également un predict_file pour prédire plusieurs images, et un predict_tile pour faire une prediction sur une très grande image.