import torch
import cv2
import json

model = torch.hub.load('ultralytics/yolov5', 'custom', path='ml_solitaire\yolov5v2\cardrecognizer.pt')

model.conf = 0.7


img = cv2.imread('ml_solitaire\yolov5v2\testing\tBillede1.jpg')[:, :, ::-1]


results = model(img)
resultsPanda = results.pandas().xyxy[0].to_json(orient="records")
resultsJSON = json.loads(resultsPanda)

print(resultsJSON)