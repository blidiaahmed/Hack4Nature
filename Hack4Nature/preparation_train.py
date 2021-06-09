from deepforest import utilities
import pandas as pd
import glob


def preparation_csv(path_to_target = './'):
    '''
    prepare le fichier csv pour le training du model
    '''
    path_to_file_list = glob.glob( path_to_target+'*.xml' )
    
    liste = []
    
    for path_to_file in path_to_file_list:
        liste.append(utilities.xml_to_annotations(path_to_file))
        
    return pd.concat(liste).reset_index(drop = True)