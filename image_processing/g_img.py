from cv2 import cv2
import numpy as np
import os
from g_shared import *
from objects import *
from enum import Enum
# if you don't start the directory at cdio_backend, check win/linux/etc. and set base_path appropriately
# base_path = os.getcwd()

# global variables
g_threshold = 0.70
g_threshold_rank = 0.50
g_threshold_suit = 0.70

# contours threshold
g_lower_threshold = 170
g_upper_threshold = 255

# an image should be resized to around this resolution
g_img_ideal_color = (1086, 2048, 3)


class CardType(Enum):
    SUIT = 1
    RANK = 2


class Suits(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4


class Ranks(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13



# Ranks by color
__tmpl_rank_2 = cv2.imread(path_template_rank_2, cv2.IMREAD_COLOR)
__tmpl_rank_3 = cv2.imread(path_template_rank_3, cv2.IMREAD_COLOR)
__tmpl_rank_4 = cv2.imread(path_template_rank_4, cv2.IMREAD_COLOR)
__tmpl_rank_5 = cv2.imread(path_template_rank_5, cv2.IMREAD_COLOR)
__tmpl_rank_6 = cv2.imread(path_template_rank_6, cv2.IMREAD_COLOR)
__tmpl_rank_7 = cv2.imread(path_template_rank_7, cv2.IMREAD_COLOR)
__tmpl_rank_8 = cv2.imread(path_template_rank_8, cv2.IMREAD_COLOR)
__tmpl_rank_9 = cv2.imread(path_template_rank_9, cv2.IMREAD_COLOR)
__tmpl_rank_10 = cv2.imread(path_template_rank_10, cv2.IMREAD_COLOR)
__tmpl_rank_jack = cv2.imread(path_template_rank_jack, cv2.IMREAD_COLOR)
__tmpl_rank_queen = cv2.imread(path_template_rank_queen, cv2.IMREAD_COLOR)
__tmpl_rank_king = cv2.imread(path_template_rank_king, cv2.IMREAD_COLOR)
__tmpl_rank_ace = cv2.imread(path_template_rank_ace, cv2.IMREAD_COLOR)


# Suits
__tmpl_suit_club = cv2.imread(path_template_suit_club, cv2.IMREAD_COLOR)
__tmpl_suit_diamond = cv2.imread(path_template_suit_diamond, cv2.IMREAD_COLOR)
__tmpl_suit_heart = cv2.imread(path_template_suit_heart, cv2.IMREAD_COLOR)
__tmpl_suit_spade = cv2.imread(path_template_suit_spade, cv2.IMREAD_COLOR)

club = TemplateType(__tmpl_suit_club, CardType.SUIT, Suits.CLUB, g_threshold)

diamond = TemplateType(__tmpl_suit_diamond, CardType.SUIT,
                       Suits.DIAMOND, g_threshold)

heart = TemplateType(__tmpl_suit_heart, CardType.SUIT,
                     Suits.HEART, g_threshold)

spade = TemplateType(__tmpl_suit_spade, CardType.SUIT,
                     Suits.SPADE, g_threshold)

# Rank Templatetypes
ace = TemplateType(__tmpl_rank_ace, CardType.RANK, Ranks.ACE, g_threshold)
two = TemplateType(__tmpl_rank_2, CardType.RANK, Ranks.TWO, g_threshold)
three = TemplateType(__tmpl_rank_3, CardType.RANK, Ranks.THREE, g_threshold)
four = TemplateType(__tmpl_rank_4, CardType.RANK, Ranks.FOUR, g_threshold)
five = TemplateType(__tmpl_rank_5, CardType.RANK, Ranks.FIVE, g_threshold)
six = TemplateType(__tmpl_rank_6, CardType.RANK, Ranks.SIX, g_threshold)
seven = TemplateType(__tmpl_rank_7, CardType.RANK, Ranks.SEVEN, g_threshold)
eight = TemplateType(__tmpl_rank_8, CardType.RANK, Ranks.EIGHT, g_threshold)
nine = TemplateType(__tmpl_rank_9, CardType.RANK, Ranks.NINE, g_threshold)
ten = TemplateType(__tmpl_rank_10, CardType.RANK, Ranks.TEN, g_threshold)
jack = TemplateType(__tmpl_rank_jack, CardType.RANK, Ranks.JACK, g_threshold)
queen = TemplateType(__tmpl_rank_queen, CardType.RANK, Ranks.QUEEN, g_threshold)
king = TemplateType(__tmpl_rank_king, CardType.RANK, Ranks.KING, g_threshold)

g_templates = [club, diamond, heart, spade, ace, two, three,
               four, five, six, seven, eight, nine, ten, jack, queen, king]

