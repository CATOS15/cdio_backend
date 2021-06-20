import torch
import cv2
import json
import numpy
import os
import image_processing.objects as obj
import image_processing.g_img as g_img
import ml_solitaire.yolov5v2.result as mapcards


#ML model loading and confidence
model = torch.hub.load('ultralytics/yolov5', 'custom', path='ml_solitaire\yolov5v2\cardrecognizer.pt')
model.conf = 0.7
#img = cv2.imread('ml_solitaire/yolov5v2/testing/*.jpg')[:, :, ::-1]

#paths for images
path = 'ml_solitaire/testing/RandomImages'

#loading all images in a folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))[:, :, ::-1]
        if img is not None:
            images.append({'filename':filename, 'image':img})
    return images



#test RandomImages folder
images = load_images_from_folder(path)

for image in images:
    values = []

    results = model(image['image'])
    resultsPanda = results.pandas().xyxy[0].to_json(orient="records")
    resultsJSON = json.loads(resultsPanda)
    values.append(image['filename'])
    for result in resultsJSON:
        name = result["name"]
        conf = result["confidence"]
        values.append({name,(round(conf, 2))})
    print(values)
    
#print(images)

# 1. load alle billeder med navne
# 2. gå igennem alle billeder og find kort værdier og confidence
# 3. find gennemsnits confidence og fjern dublicates
# 3.1 EXTRA find højeste og laveste konfidens
# 4. gem værdier så de kan manuelt checkes. 

#print(resultsJSON)