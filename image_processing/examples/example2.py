import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

path_card = 'examples/card3/3_diamonds_hearts_whole.png'
path_template_number = 'examples/card2/3_diamonds_number_template.png'
path_template_suit_diamonds = 'examples/card2/3_diamonds_suit_template.png'
path_template_suit_hearts = 'examples/card3/3_hearts_suit.png'

res_number = 'examples/card2/res.png'

# card color
img_color = cv2.imread(path_card)
img_grey = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

template_number = cv2.imread(path_template_number, 0)
template_suit_heart = cv2.imread(path_template_suit_hearts,0)
template_suit_diamonds = cv2.imread(path_template_suit_diamonds, 0)

w_number, h_number = template_number.shape[::-1]
w_color, w_color = template_suit_diamonds.shape[::-1]

suit_diamonds_match = cv2.matchTemplate(img_grey, template_suit_diamonds,cv2.TM_CCOEFF_NORMED)
number_match = cv2.matchTemplate(img_grey, template_number, cv2.TM_CCOEFF_NORMED)
suit_heart_match = cv2.matchTemplate(img_grey, template_suit_heart, cv2.TM_CCOEFF_NORMED)


threshold = 0.90 
loc_number = np.where(number_match >= threshold)
for pt in zip(*loc_number[::-1]):
    cv2.rectangle(img_color, pt,(pt[0] + w_number, pt[1] + h_number), (0, 0, 255), 2)

loc_suit_diamonds = np.where(suit_diamonds_match >= threshold)
for pt in zip(*loc_suit_diamonds[::-1]):
    cv2.rectangle(img_color, pt,(pt[0] + w_color, pt[1] + w_color), (0, 255, 0), 2)

loc_suit_heart = np.where(suit_heart_match >= threshold)
for pt in zip(*loc_suit_heart[::-1]):
    cv2.rectangle(img_color, pt,(pt[0] + w_color, pt[1] + w_color), (255, 0, 0), 2)

cv2.imwrite(res_number, img_color)


#Fun stuff
#Check Differnet algorithms
#Try different Images (now)
#Think creative stuff and poop???

#rewrite to look for highest threshold
#recognize coloumns?
#check match multiple different numbers/suits