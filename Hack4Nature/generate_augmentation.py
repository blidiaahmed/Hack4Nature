import numpy as np
import pandas as pd
import os

from Hack4Nature.generate_csv import generate_csv_training, generate_csv_evaluation
from Hack4Nature import data_augmentation


def apply_augmentations(df):
    '''
        Applies augmentations to a given dataFrame containing annotations from a single image.
    
    '''
    #We might choose to apply some or all the augmentation, think about it !!!
    
    df_flip = data_augmentation.horizontal_flip(df)
    df_mirror = data_augmentation.vertical_flip(df)
    df_bright = data_augmentation.bright_change(df)
    df_color = data_augmentation.color_change(df)    
    
    return pd.concat([df_flip, df_mirror, df_bright, df_color])


def generate_csv_augmentation(annotations_df, 
                              path_images_augmented = 'raw_data/data_images_augmented/',
                              csv_name='csv_full_training_set.csv'):
    '''
        Génère un csv des images augmentées à partir du dataFrame des annotations des images de base.
        annotations_df: dataFrame des annotations des images non augmentées ou images de base
        path_images_augmented: répertoir de sauvegarde des images augmentées et du csv généré correspondant
        csv_name: nom du fichier csv généré
    '''
    #dfa = annotations_df.loc[:3,:].copy()
    dfa = annotations_df.copy()
    
    # get unique image names/paths
    unique_image_paths = dfa.image_path.unique()
    
    # split the dfa per unique image names and apply augmentation df
    list_small_df = []
    for image_path in unique_image_paths:
        
        small_df = dfa.loc[dfa.image_path == image_path]
        small_df.reset_index(drop=True, inplace=True) 
        
        aug_df = apply_augmentations(small_df)
        
        aug_df['image_path'] = aug_df['image_path'].apply(os.path.basename)
        
        list_small_df.append(aug_df)
    
    
    #concat list of augmented small list_small_df to a single dataframe large_df   
    list_df = pd.concat(list_small_df).reset_index(drop = True)
    large_df = pd.concat([dfa, list_df]).reset_index(drop = True)
    
    #converted dataframe to csv file and saved alongside the images
    large_csv = os.path.join(path_images_augmented, csv_name)
    large_df.to_csv(large_csv, index=False)
    
    #break
    return large_df, large_csv



if __name__ == "__main__":
    df, _ = generate_csv_training(path_images_csv='raw_data/data_images/',
                                path_xml='raw_data/data_xml/',
                                csv_name='csv_test_aug.csv')
    
    augmented_df, augmented_csv = generate_csv_augmentation(df)
    
    
