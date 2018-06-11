# Image_Room_Classification

## Download the dataset

This room classification is based on image recognition and tensorflow retraining.  
At first, we use image from ImageNet to feed the retrain algorithm.  

In order to download the dataset, you need to go to :  
http://image-net.org/  
  
Then you can choose the branch that interest you and download the "synset.txt" file. This file containes urls of photos for this label. Not every url is a valid one, and our script manages most of errors.    
Make sure the .txt file begin with "wantedLabel_"  

Finally, you can launch  
``` python download_url_images.py```  

