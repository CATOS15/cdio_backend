import cv2
import numpy as np
#tpe = template
#Suits
path_template_suit_diamonds = 'image_processing/templates/suits/3_diamonds_suit_template.png'
path_template_suit_hearts = 'image_processing/templates/suits/3_hearts_suit_template.png'
# path_tpe_suit_spades = ''
# path_tpe_suit_clubs = ''

#global variables
g_threshold = 0.80
g_red_square = (0, 0, 255)
g_green_square = (0, 255, 0)
g_blue_square = (255, 0, 0)

#Numbers Red
path_template_number = 'image_processing/templates/number/3_red_diamond_number_template.png'
# path_tpe_ace = ''
# path_tpe_2 = ''
# path_tpe_3 = ''
# path_tpe_4 = ''
# path_tpe_5 = ''
# path_tpe_6 = ''
# path_tpe_7 = ''
# path_tpe_8 = ''
# path_tpe_9 = ''
# path_tpe_10 = ''
# path_tpe_jack = ''
# path_tpe_queen = ''
# path_tpe_king = ''

#Numbers Black <- hopefully we can delete this

#Testing
path_card = 'image_processing/templates/test/3_diamonds_hearts_whole.png' #remove, when we can recive input, for testing only
g_img_color = cv2.imread(path_card)
img_grey = cv2.cvtColor(g_img_color, cv2.COLOR_BGR2GRAY)

#Suits
template_suit_heart = cv2.imread(path_template_suit_hearts,0)
template_suit_diamonds = cv2.imread(path_template_suit_diamonds, 0)


#Numbers
template_number = cv2.imread(path_template_number, 0)

#templates sizes
w_number, h_number = template_number.shape[::-1]
w_suit_diamonds, h_suit_diamonds = template_suit_diamonds.shape[::-1]
w_suit_heart, h_suit_heart = template_suit_heart.shape[::-1]


#Algorithm
suit_heart_match = cv2.matchTemplate(img_grey, template_suit_heart, cv2.TM_CCOEFF_NORMED)
suit_diamonds_match = cv2.matchTemplate(img_grey, template_suit_diamonds,cv2.TM_CCOEFF_NORMED)
number_match = cv2.matchTemplate(img_grey, template_number, cv2.TM_CCOEFF_NORMED)


#store results
result_image = 'image_processing/templates/card/result/res.png'