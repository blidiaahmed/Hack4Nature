# Information sur Deepforest

## Check patch size
The prebuilt model was trained on 10cm data at 400px crops. The model is sensitive to predicting to new image resolutions that differ. We have found that increasing the patch size works better on higher quality data. For example, here is a drone collected data at the standard 400px

## Train
### csv_file
Path to csv_file for training annotations. Annotations are .csv files with headers image_path, xmin, ymin, xmax, ymax, label. image_path are relative to the root_dir. For example this file should have entries like myimage.tif not /path/to/myimage.tif

## Training
The prebuilt models will always be improved by adding data from the target area. In our work, we have found that even one hour’s worth of carefully chosen hand-annotation can yield enormous improvements in accuracy and precision. We envision that for the majority of scientific applications at least some fine-tuning of the prebuilt model will be worthwhile. When starting from the prebuilt model for training, we have found that 5-10 epochs is sufficient. We have never seen a retraining task that improved after 10-30 epochs, but it is possible if there are very large datasets with very diverse classes.

## Google Collab Demo on model Training

https://colab.research.google.com/drive/1AJUcw5dEpXeDPHd0sotAz5lpWedFYSIL#offline=true&sandboxMode=true