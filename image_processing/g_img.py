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
__tmpl_suit_heart = cv2.imread(path_template_suit_heart, 0)
__tmpl_suit_diamonds = cv2.imread(path_template_suit_diamonds, 0)

# Template for Numbers
__tmpl_rank_three = cv2.imread(path_template_number, 0)



#Suits
# clubs = TemplateType(CardType.Suit, Suit.CLUBS, g_threshold)
diamonds = TemplateType(__tmpl_suit_diamonds,CardType.SUIT, Suits.DIAMOND, g_threshold)
hearts = TemplateType(__tmpl_suit_heart, CardType.SUIT, Suits.HEART, g_threshold)
# spades = TemplateType(CardType.Suit, Suit.SPADES, g_threshold)

#numbers
# ace = TemplateType(CardType.Rank, 1, g_threshold)
# two = TemplateType(CardType.Rank, 2, g_threshold)
three = TemplateType(__tmpl_rank_three, CardType.RANK, 3, g_threshold)
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

g_templates = [hearts, three]
# g_templates = [clubs, diamonds, hearts, spades, ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king]

