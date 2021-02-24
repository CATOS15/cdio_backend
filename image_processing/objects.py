import cv2

from enum import Enum

Suit = Enum('Suits', 'Spade Heart Diamonds Club')
Cards = Enum(
    'Cards', 'Ace Two Three Four Five Six Seven Eight Nine Ten Eleven Twelf Thirteen')

# Algorithm for template matching
g_match_alg = cv2.TM_CCOEFF_NORMED

class DrawSquare:
    def __init__(self, color, thicc):
        self.color = color
        self.thicc = thicc


class TemplateInfo:
    def __init__(self, templ_image, threshold, width, height, drawSquare):
        self.templ_image = templ_image
        self.threshold = threshold
        self.width = width
        self.height = height
        self.drawSquare = drawSquare

    def compare_template(self, img_grey):
     self.templ_image = cv2.bitwise_not(self.templ_image)
     cv2.imwrite("image_processing/templates/card/result/templ_test.png", self.templ_image)
     return cv2.matchTemplate(img_grey, self.templ_image, g_match_alg) 