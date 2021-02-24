from cv2 import cv2
import numpy as np
import os
from objects import *
# if you don't start the directory at cdio_backend, check win/linux/etc. and set base_path appropriately
# base_path = os.getcwd()
# Suits
path_template_suit_diamonds = 'image_processing/templates/suits/3_diamonds_suit_template.png'
path_template_suit_hearts = 'image_processing/templates/suits/3_hearts_suit_template.png'
# path_tpe_suit_spades = ''
# path_tpe_suit_clubs = ''

# global variables
g_threshold = 0.80
g_red_square = (0, 0, 255)
g_green_square = (0, 255, 0)
g_blue_square = (255, 0, 0)

# Numbers Red
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

# Numbers Black <- hopefully we can delete this

# Testing
# for testing only
path_card = './image_processing/templates/test/3_diamonds_hearts_whole.png'
g_img_color = cv2.imread(path_card)
g_img_grey = cv2.cvtColor(g_img_color, cv2.COLOR_BGR2GRAY)

# an image should be resized to around this resolution
g_img_ideal_color = (1086, 2048, 3)

# Suits
__template_suit_heart = cv2.imread(path_template_suit_hearts, 0)
__template_suit_diamonds = cv2.imread(path_template_suit_diamonds, 0)


# Numbers
__template_number = cv2.imread(path_template_number, 0)

# templates sizes
__w_number, __h_number = __template_number.shape[::-1]
__w_suit_diamond, __h_suit_diamond = __template_suit_diamonds.shape[::-1]
__w_suit_heart, __h_suit_heart = __template_suit_heart.shape[::-1]


# Templates as Objects
__tmpl_heart = TemplateInfo(__template_suit_heart, g_threshold,
                            __w_suit_heart, __h_suit_heart, DrawSquare(g_red_square, 2))

__tmpl_diamond = TemplateInfo(__template_suit_diamonds, g_threshold,
                              __w_suit_diamond, __h_suit_diamond, DrawSquare(g_green_square, 2))
__tmpl_three = TemplateInfo(
    __template_number, 0.65, __w_number, __h_number, DrawSquare(g_blue_square, 2))

__tmpl_number_objects = {Cards.Three:__tmpl_three}

g_templ_objs = {'heart': __tmpl_heart,
                'diamond': __tmpl_diamond, 'number': __tmpl_number_objects}

# store results
result_image = 'image_processing/templates/card/result/res.png'
