import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# path_card = 'examples/card3/3_diamonds_hearts_whole.png'
path_card = 'image_processing/examples/card3/test_3_diamonds_both.png'

path_template_number = 'image_processing/examples/card2/3_diamonds_number_template.png'
path_template_suit_diamonds = 'image_processing/examples/card2/3_diamonds_suit_template.png'
path_template_suit_hearts = 'image_processing/examples/card3/3_hearts_suit.png'

res_number = 'image_processing/examples/card2/res.png'

# card color
img_color = cv2.imread(path_card)
img_grey = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

template_number = cv2.imread(path_template_number, 0)
template_suit_heart = cv2.imread(path_template_suit_hearts,0)
template_suit_diamonds = cv2.imread(path_template_suit_diamonds, 0)

w_number, h_number = template_number.shape[::-1]
w_suit_diamonds, h_suit_diamonds = template_suit_diamonds.shape[::-1]
w_suit_heart, h_suit_heart = template_suit_heart.shape[::-1]

suit_heart_match = cv2.matchTemplate(img_grey, template_suit_heart, cv2.TM_CCOEFF_NORMED)
suit_diamonds_match = cv2.matchTemplate(img_grey, template_suit_diamonds,cv2.TM_CCOEFF_NORMED)
number_match = cv2.matchTemplate(img_grey, template_number, cv2.TM_CCOEFF_NORMED)


threshold = 0.90 

red_square = (0, 0, 255)
green_square = (0, 255, 0)
blue_square = (255, 0, 0)

def locate_figure(template_match,l_threshold, width, height, color):
    thicc = 2
    loc = np.where(template_match >= l_threshold)
    for pt in zip(*loc[::-1]):
            cv2.rectangle(img_color, pt,(pt[0] + width, pt[1] + height), color, thicc)

locate_figure(number_match, threshold, w_number, h_number, red_square)
locate_figure(suit_diamonds_match, threshold, w_suit_diamonds, h_suit_diamonds, green_square)
locate_figure(suit_heart_match, threshold, w_suit_heart, h_suit_heart, blue_square)

cv2.imwrite(res_number, img_color)


#Fun stuff
#Check Differnet algorithms
#Try different Images (now)
#Think creative stuff and poop???

#rewrite to look for highest threshold
#recognize coloumns?
#check match multiple different numbers/suits
#try checking w. black and red card