from deepforest import utilities
import pandas as pd
import glob
import os


def generate_csv_training(path_images_csv = 'raw_data/data_images/',
                          path_xml = 'raw_data/data_xml/',
                          csv_name = 'csv_training.csv'):
    '''
        Généner le fichier csv pour le training du model.
        Les dossiers 'data_images' et 'data_xml' contenant respectivement les images et les fichiers .xml 
        doivent être dans le répertoire raw_data.
        Les dossiers sont codés en dur juste pour l'entrainement, so no worries !!!
    '''

    #path_images_csv = 'raw_data/data_images'    
    #path_xml = 'raw_data/data_xml/'


    path_xml_list = glob.glob(path_xml+'*.xml')

    liste = []
    for path_to_file in path_xml_list:
        liste.append(utilities.xml_to_annotations(path_to_file))
    
    # add image_path
    df = pd.concat(liste).reset_index(drop = True)
    df['image_path'] = df['image_path'].apply(lambda x: x + '.png')

    
    # converted dataframe to file and saved alongside the images
    print(os.path.join(path_images_csv, csv_name))
    csv = os.path.join(path_images_csv, csv_name)
    df.to_csv(csv, index=False)
    
    #df et path csv sont retournés actuellement pour le test, mais return peut être None
    return df, csv



def generate_csv_evaluation(xml_path = 'raw_data/data_xml/', 
                            csv_name = 'csv_eval.csv'):
    """
        test: Generates a csv file from corresponding xml file 
        and save in 'data_csv' folder in raw_data folder
        for model evaluation or prediction
    """
    
    # df is the DataFrame containing the annotations
    df = utilities.xml_to_annotations(xml_path)
    df['image_path'] = df['image_path'].apply(lambda x: x + '.png')
       
    csv = os.path.join(os.path.dirname(xml_path), csv_name)    
    df.to_csv(csv, index=False)
    
    #df et path csv sont retournés actuellement pour le test, mais return peut être None
    return df, csv


if __name__ == "__main__":
    df, annotations_path = generate_csv_training(csv_name="csv_name.csv")
    print(df.head(3))
    print(annotations_path)
    
    print('==============================================================')
    xml_path = 'raw_data/data_xml/labels_43.2863_5.4229_Fwn6Col.xml'
    df_csv, csv_eval = generate_csv_evaluation(xml_path)
    print(df_csv.head(3))
    print(csv_eval)


