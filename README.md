# Image_Room_Classification

## Download the dataset

This room classification is based on image recognition and tensorflow retraining.  
At first, we use image from ImageNet to feed the retrain algorithm.  

In order to download the dataset, you need to go to :  
http://image-net.org/  
  
Then you can choose the branch that interest you and download the "synset.txt" file under the "get_dataset" folder. This file containes urls of photos for this label. Not every url is a valid one, and our script manages most of the errors.    
Make sure the .txt file begin with "wantedLabel_"  

Finally, you can launch  
``` 
cd get_dataset  
python3 download_url_images.py```  

