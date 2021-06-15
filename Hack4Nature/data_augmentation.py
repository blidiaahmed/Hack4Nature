from PIL import Image, ImageOps
import os
import matplotlib.pyplot as plt

import imageio
import imgaug as ia
import imgaug.augmenters as iaa

# test 

from deepforest import utilities
from Hack4Nature.show_image import image_label

def horizontal_flip(data,
                    path_data_images = 'raw_data/data_images/',
                    path_images_augmented = 'raw_data/data_images_augmented/'):
    """
    prend un dataframe avec le chemin de l'image et les coordonnées des annotations et renvoie
    la transformée horizontal de cette image avec la transformée verticale des annotations
    """
     
    
    # On recupère l'image
    image_0 = os.path.join(path_data_images, data['image_path'][0]) 
    print('==============================================================')
    print('Horizontal flip augmentation in progress ...')
    im = Image.open(image_0)
    
    
    
    # On recupère le chemin d'accès
    directory = os.path.dirname(image_0)#data['image_path'][0])
    base = os.path.basename(image_0)#data['image_path'][0])
    
    # On crée la transformation
    im_flip = ImageOps.flip(im)
    
    # On sauvegarde la transformation dans le même repertoire et on la nomme flip_nom_original
    # im_flip.save(os.path.join(directory,f"flip_{base}"), format="png")
    
    im_flip.save(os.path.join(path_images_augmented,f"flip_{base}"), format="png")
    
    # On récupère sa dimension
    image_shape = plt.imread(image_0).shape#data['image_path'][0]).shape
    print(f'shape {image_shape}')
    
    # On adapate les annotations
    data_flip = data.copy()
    
    data_flip['image_path'] = os.path.join(directory,f"flip_{base}")
    
    data_flip['ymin'] = image_shape[1] - data['ymax']
    data_flip['ymax'] = image_shape[1] - data['ymin']
    
    # On retourne un DataFrame près à l'emploi
    return data_flip

def vertical_flip(data,
                    path_data_images = 'raw_data/data_images/',
                    path_images_augmented = 'raw_data/data_images_augmented/'):
    """
    prend un dataframe avec le chemin de l'image et les coordonnées des annotations et renvoie
    la transformée verticale de cette image avec la transformée horizontale des annotations
    """
     
    
    # On recupère l'image
    image_0 = os.path.join(os.path.dirname(path_data_images), data['image_path'][0]) 
    print('==============================================================')
    print('Vertical flip augmentation in progress ...')
    im = Image.open(image_0)
    #print(f'im: {im}')
     
        
    # On recupère le chemin d'accès
    directory = os.path.dirname(image_0)#data['image_path'][0])
    base = os.path.basename(image_0)#data['image_path'][0])
    
    # On crée la transformation
    im_mirror = ImageOps.mirror(im)
    
    # On sauvegarde la transformation dans le même repertoire et on la nomme miror_nom_original
    # im_mirror.save(os.path.join(directory,f"miror_{base}"), format="png")
    im_mirror.save(os.path.join(path_images_augmented,f"miror_{base}"), format="png")
    
    # On récupère sa dimension
    image_shape = plt.imread(image_0).shape#data['image_path'][0]).shape
    
    # On adapate les annotations
    data_miror = data.copy()
    
    data_miror['image_path'] = os.path.join(directory,f"miror_{base}")
    
    data_miror['xmin'] = image_shape[0] - data['xmax']
    data_miror['xmax'] = image_shape[0] - data['xmin']
    
    # On retourne un DataFrame près à l'emploi
    return data_miror



def bright_change(data,
                  path_data_images = 'raw_data/data_images/',
                  path_images_augmented = 'raw_data/data_images_augmented/'):
    """
        Ajoute un docstring !!!
    """
    
    #image = imageio.imread(data['image_path'][0])
    #print(type(image))
    image_path = os.path.join(os.path.dirname(path_data_images), data['image_path'][0]) 
    print('==============================================================')
    print('Bightness augmentation in progress ...')
    image_0 = imageio.imread(image_path)
    
    contrast=iaa.GammaContrast(gamma=(0.5, 2.0))
    contrast_image =contrast.augment_image(image_0)
    
    directory = os.path.dirname(image_path)#data['image_path'][0])
    base = os.path.basename(image_path)#data['image_path'][0])
    
    # imageio.imwrite(os.path.join(directory,f"contrast_{base}"), contrast_image)
    imageio.imwrite(os.path.join(path_images_augmented,f"contrast_{base}"), contrast_image)
    
    data_bright = data.copy()
    
    data_bright['image_path'] = os.path.join(directory,f"contrast_{base}")
    
    return data_bright



def color_change(data,
                 path_data_images = 'raw_data/data_images/',
                 path_images_augmented = 'raw_data/data_images_augmented/'):
    """
        Ajoute un docstring !!!
    """
    
    #image = imageio.imread(data['image_path'][0])
    image_path = os.path.join(os.path.dirname(path_data_images), data['image_path'][0]) 
    print('==============================================================')
    print('Color augmentation in progress ...')
    image_0 = imageio.imread(image_path)    
    
    contrast=iaa.GammaContrast(gamma=(0.5, 2.0), per_channel=True)
    contrast_image =contrast.augment_image(image_0)
    
    directory = os.path.dirname(image_path)#data['image_path'][0])
    base = os.path.basename(image_path)#data['image_path'][0])
    
    # imageio.imwrite(os.path.join(directory,f"color_{base}"), contrast_image)
    imageio.imwrite(os.path.join(path_images_augmented,f"color_{base}"), contrast_image)
    
    data_color = data.copy()
    
    data_color['image_path'] = os.path.join(directory,f"color_{base}")
    
    return data_color


