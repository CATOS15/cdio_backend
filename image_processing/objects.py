import cv2
from g_shared import *
from img_contour import *
# from img_compare import template_match_alg

# Algorithm for template matching

# g_match_alg = cv2.TM_SQDIFF


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

    # def compare_template(self, washed_img):                        
    #     flipped = cv2.bitwise_not(self.templ_image)
    #     blur = cv2.GaussianBlur(flipped, (5, 5), 0)
    #     ret, th = cv2.threshold(
    #         blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #     cv2.imwrite(path_template_sp1.format(0), th)
    #     return cv2.matchTemplate(washed_img, th, template_match_alg)

        # return cv2.matchTemplate(washed_img, self.templ_image, g_match_alg)


class Flow:
    def __init__(self, cb_wash, cb_contour, cb_cut_suit_rank, cb_compare_by_template):
        self.cb_wash = cb_wash
        self.cb_contour = cb_contour
        self.cb_cut_suit_rank = cb_cut_suit_rank
        # self.cb_resolution = cb_resolution
        self.cb_compare_by_template = cb_compare_by_template

    
    def execute_wash(self, ready_img, flow_two_contours):
        return self.cb_wash(ready_img, flow_two_contours)

        
    def execute_contour(self, alg1, alg2, img_thresh, img_color=None):
        return self.cb_contour(alg1, alg2, img_thresh,  img_color)

    def execute_cut_suit_rank(self, img_contours, alg1, alg2):
        return self.cb_cut_suit_rank(img_contours, alg1, alg2)

    
    #Implement resolution here
    # def execute_resolution(self, )
    
    def execute_compare_by_template(self, cards, ideal_image):
        return self.cb_compare_by_template(cards, ideal_image)

#either suit or rank, type: rank/suit, value = actual value
class TemplateType:
    def __init__(self, img, type, value, threshold):
        self.img = img
        self.type = type
        self.value = value
        self.threshold = threshold


    def suit_match(self, type):
        return self.type == type
    
    def higher_threshold(self, threshold):
        return self.type_threshold < threshold

    def add_success(self, contour):
        self.contour = contour


class Foo:
    def __init__(self, minMaxLoc, suit):
        self.minMaxLoc = minMaxLoc
        self.suit = suit