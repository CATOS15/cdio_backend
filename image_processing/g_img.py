from cv2 import cv2
import numpy as np
import os
from g_shared import *
from objects import *
from enum import Enum
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

#contours threshold
g_lower_threshold = 170
g_upper_threshold = 255

# an image should be resized to around this resolution
g_img_ideal_color = (1086, 2048, 3)

class CardType(Enum):
    SUIT = 1
    RANK = 2

class Suits(Enum):
    CLUBS = 1
    DIAMOND = 2
    HEART = 3    
    SPADES = 4


# Template for x
__template_suit_heart = cv2.imread(path_template_suit_heart, 0)
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


#Suits
# clubs = TemplateType(CardType.Suit, Suit.CLUBS, g_threshold)
# diamonds = TemplateType(CardType.Suit, Suit.DIAMOND, g_threshold)
hearts = TemplateType(__template_suit_heart, CardType.SUIT, Suits.HEART, g_threshold)
# spades = TemplateType(CardType.Suit, Suit.SPADES, g_threshold)

#numbers
# ace = TemplateType(CardType.Rank, 1, g_threshold)
# two = TemplateType(CardType.Rank, 2, g_threshold)
# three = TemplateType(CardType.Rank, 3, g_threshold)
# four = TemplateType(CardType.Rank, 4, g_threshold)
# five = TemplateType(CardType.Rank, 5, g_threshold)
# six = TemplateType(CardType.Rank, 6, g_threshold)
# seven = TemplateType(CardType.Rank, 7, g_threshold)
# eight = TemplateType(CardType.Rank, 8, g_threshold)
# nine = TemplateType(CardType.Rank, 9, g_threshold)
# ten = TemplateType(CardType.Rank, 10, g_threshold)
# jack = TemplateType(CardType.Rank, 11, g_threshold)
# queen = TemplateType(CardType.Rank, 12, g_threshold)
# king = TemplateType(CardType.Rank, 13, g_threshold)

g_templates = [hearts]
# g_templates = [clubs, diamonds, hearts, spades, ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king]

