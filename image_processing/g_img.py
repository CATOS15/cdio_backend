from cv2 import cv2
import numpy as np
import os
from g_shared import *
from objects import *
# if you don't start the directory at cdio_backend, check win/linux/etc. and set base_path appropriately
# base_path = os.getcwd()

# global variables
g_threshold = 0.85
g_red_square = (0, 0, 255)
g_green_square = (0, 255, 0)
g_blue_square = (255, 0, 0)

g_ideal_card_suit_width = 5/55
g_ideal_card_suit_height = 7/55
g_ideal_card_number_width = (7)/55
g_ideal_card_number_height = (10)/55

# an image should be resized to around this resolution
g_img_ideal_color = (1086, 2048, 3)


# Template for Suits
__template_suit_heart = cv2.imread(path_template_suit_hearts, 0)
__template_suit_diamonds = cv2.imread(path_template_suit_diamonds, 0)

# Template for Numbers
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
    __template_number, g_threshold, __w_number, __h_number, DrawSquare(g_blue_square, 2))


# g_templ_objs = {'heart': __tmpl_heart,
#                 'diamond': __tmpl_diamond, 'number': __tmpl_number_objects}

g_suits = [__tmpl_heart]
g_numbers = [__tmpl_three]



