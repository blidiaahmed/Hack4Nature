import matplotlib.pyplot as plt
import pandas as pd
import cv2

def image_label(data):
    '''
    prend le dataframe d'une seul image avec les coordonnées des labels
    '''
    image = plt.imread(data['image_path'][0])
    
    for index, row in data[['xmin','ymin','xmax','ymax']].iterrows():
        cv2.rectangle(image, (int(row["xmin"]), int(row["ymin"])), (int(row["xmax"]), int(row["ymax"])), color=(255,255,0), thickness=2, lineType=cv2.LINE_AA)
    
    plt.figure(figsize=(10,10))    
    
    plt.imshow(image)
    