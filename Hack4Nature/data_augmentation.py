from PIL import Image, ImageOps
import os
import matplotlib.pyplot as plt

import imageio
import imgaug as ia
import imgaug.augmenters as iaa

# test 

from deepforest import utilities
from Hack4Nature.show_image import image_label

def horizontal_flip(data):
    """
    prend un dataframe avec le chemin de l'image et les coordonnées des labels et renvoie
    la transformée horizontal de cette image avec la transformée verticale des annotations
    """
    path_images_augmented = '../raw_data/data_images_augmented/' 
    
    # On recupère l'image
    im = Image.open(data['image_path'][0])
    
    
    # On recupère le chemin d'accès
    directory = os.path.dirname(data['image_path'][0])
    base = os.path.basename(data['image_path'][0])
    
    # On crée la transformation
    im_flip = ImageOps.flip(im)
    
    # On sauvegarde la transformation dans le même repertoire et on la nomme flip_nom_original
    # im_flip.save(os.path.join(directory,f"flip_{base}"), format="png")
    
    im_flip.save(os.path.join(path_images_augmented,f"flip_{base}"), format="png")
    
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
    path_images_augmented = '../raw_data/data_images_augmented/' 
    
    # On recupère l'image
    im = Image.open(data['image_path'][0])
    
    # On recupère le chemin d'accès
    directory = os.path.dirname(data['image_path'][0])
    base = os.path.basename(data['image_path'][0])
    
    # On crée la transformation
    im_mirror = ImageOps.mirror(im)
    
    # On sauvegarde la transformation dans le même repertoire et on la nomme miror_nom_original
    # im_mirror.save(os.path.join(directory,f"miror_{base}"), format="png")
    im_mirror.save(os.path.join(path_images_augmented,f"miror_{base}"), format="png")
    
    # On récupère sa dimension
    image_shape = plt.imread(data['image_path'][0]).shape
    
    # On adapate les annotations
    data_miror = data.copy()
    
    data_miror['image_path'] = os.path.join(directory,f"miror_{base}")
    
    data_miror['xmin'] = image_shape[0] - data_miror['xmin']
    data_miror['xmax'] = image_shape[0] - data_miror['xmax']
    
    # On retourne un DataFrame près à l'emploi
    return data_miror

def bright_change(data):
    
    path_images_augmented = '../raw_data/data_images_augmented/' 
    
    image = imageio.imread(data['image_path'][0])
    contrast=iaa.GammaContrast(gamma=(0.5, 2.0))
    contrast_image =contrast.augment_image(image)
    
    directory = os.path.dirname(data['image_path'][0])
    base = os.path.basename(data['image_path'][0])
    
    # imageio.imwrite(os.path.join(directory,f"contrast_{base}"), contrast_image)
    imageio.imwrite(os.path.join(path_images_augmented,f"contrast_{base}"), contrast_image)
    
    data_bright = data.copy()
    
    data_bright['image_path'] = os.path.join(directory,f"contrast_{base}")
    
    return data_bright

def color_change(data):
    
    path_images_augmented = '../raw_data/data_images_augmented/' 
    
    image = imageio.imread(data['image_path'][0])
    contrast=iaa.GammaContrast(gamma=(0.5, 2.0),per_channel=True)
    contrast_image =contrast.augment_image(image)
    
    directory = os.path.dirname(data['image_path'][0])
    base = os.path.basename(data['image_path'][0])
    
    # imageio.imwrite(os.path.join(directory,f"color_{base}"), contrast_image)
    imageio.imwrite(os.path.join(path_images_augmented,f"color_{base}"), contrast_image)
    
    data_color = data.copy()
    
    data_color['image_path'] = os.path.join(directory,f"color_{base}")
    
    return data_color


