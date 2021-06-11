from PIL import Image, ImageOps
import os
import matplotlib.pyplot as plt

def horizontal_flip(data):
    """
    prend un dataframe avec le chemin de l'image et les coordonnées des labels et renvoie
    la transformée horizontal de cette image avec la transformée verticale des annotations
    """
    # On recupère l'image
    im = Image.open(data['image_path'][0])
    
    
    # On recupère le chemin d'accès
    directory = os.path.dirname(data['image_path'][0])
    base = os.path.basename(data['image_path'][0])
    
    # On crée la transformation
    im_flip = ImageOps.flip(im)
    
    # On sauvegarde la transformation dans le même repertoire et on la nomme flip_nom_original
    im_flip.save(os.path.join(directory,f"flip_{base}"), format="png")
    
    # On récupère sa dimension
    image_shape = plt.imread(data['image_path'][0]).shape
    
    # On adapate les annotations
    data_flip = data.copy()
    
    data_flip['image_path'] = os.path.join(directory,f"flip_{base}")
    
    data_flip['ymin'] = image_shape[1] - data_flip['ymin']
    data_flip['ymax'] = image_shape[1] - data_flip['ymax']
    
    # On retourne un DataFrame près à l'emploi
    return data_flip

def vertical_flip(data):
    """
    prend un dataframe avec le chemin de l'image et les coordonnées des labels et renvoie
    la transformée verticale de cette image avec la transformée horizontale des annotations
    """
    # On recupère l'image
    im = Image.open(data['image_path'][0])
    
    
    # On recupère le chemin d'accès
    directory = os.path.dirname(data['image_path'][0])
    base = os.path.basename(data['image_path'][0])
    
    # On crée la transformation
    im_mirror = ImageOps.mirror(im)
    
    # On sauvegarde la transformation dans le même repertoire et on la nomme miror_nom_original
    im_mirror.save(os.path.join(directory,f"miror_{base}"), format="png")
    
    # On récupère sa dimension
    image_shape = plt.imread(data['image_path'][0]).shape
    
    # On adapate les annotations
    data_miror = data.copy()
    
    data_miror['image_path'] = os.path.join(directory,f"miror_{base}")
    
    data_miror['xmin'] = image_shape[0] - data_miror['xmin']
    data_miror['xmax'] = image_shape[0] - data_miror['xmax']
    
    # On retourne un DataFrame près à l'emploi
    return data_miror
