from deepforest import utilities
import pandas as pd
import glob
import os


def generate_csv_training(path_to_target = 'raw_data/'):
    '''
        Généner le fichier csv pour le training du model.
        Les dossiers 'data_images' et 'data_xml' contenant les iamges et les fichiers .xml respectivement
        doivent etre dans le répertoire raw_data.
    '''
    #parent_folder = os.path.dirname(os.path.dirname(path_to_target))
    parent_folder = os.path.dirname(path_to_target)
    
    path_image = '/data_images/'
    path_csv = os.path.join(parent_folder, 'data_csv/')

    path_xml_list = glob.glob(path_to_target+'data_xml/*.xml')
    
    liste = []
    for path_to_file in path_xml_list:
        liste.append(utilities.xml_to_annotations(path_to_file))
    
    # add image_path
    df = pd.concat(liste).reset_index(drop = True)
    df['image_path'].apply(lambda x: path_image + x + '.npg')
    
    # converted dataframe to csv file and saved alongside the images
    csv = os.path.join(path_csv,"generated_test.csv")
    df.to_csv(csv, index=False)
    
    #df et csv sont retournés actuellement pour le test, mais return peut être None 
    return df, csv



def generate_csv_evaluation(xml_path):
    """
        test: Generates a csv file from corresponding xml file and save in 'data_csv' folder in raw_data folder
        for model evaluation or prediction
    """
    path_image = 'data_images/'
    
    # df is the DataFrame containing the annotations
    df = utilities.xml_to_annotations(xml_path)
    df['image_path'].apply(lambda x: path_image + x + '.npg')
       
    parent_folder = os.path.dirname(os.path.dirname(xml_path))
    path_csv = os.path.join(parent_folder, 'data_csv/')
    csv = os.path.join(path_csv,"csv_4_eval.csv")
    
    df.to_csv(csv, index=False)
    
    #df et csv sont retournés actuellement pour le test, mais return peut être None
    return df, csv


if __name__ == "__main__":
    path_to_raw_data = 'raw_data/'
    df, annotations_path = generate_csv_training(path_to_raw_data)
    print(df.head(3))
    print(annotations_path)
    
    print('==============================================================')
    xml_path = 'raw_data/data_xml/labels_43.2863_5.4229_Fwn6Col.xml'
    df_csv, csv_eval = generate_csv_evaluation(xml_path)
    print(df_csv.head(3))
    print(csv_eval)


