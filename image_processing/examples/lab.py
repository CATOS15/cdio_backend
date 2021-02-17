import cv2
import numpy as np
from matplotlib import pyplot as plt

img2 = cv2.imread('card.jpg', cv2.IMREAD_GRAYSCALE)
#s_img2 = 'image2'

template = cv2.imread('2_diamonds', cv2.IMREAD_GRAYSCALE)
match_method = cv2.TM_SQDIFF #minLoc

result = cv2.matchTemplate(img2, template, match_method)

_minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(result, None)



#https://docs.opencv.org/master/d9/df8/tutorial_root.html