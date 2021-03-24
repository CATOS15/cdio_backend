import cv2
from g_shared import *
from img_contour import *


# Algorithm for template matching
g_match_alg = cv2.TM_CCOEFF_NORMED
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

    def compare_template(self, washed_img):                        
        flipped = cv2.bitwise_not(self.templ_image)
        blur = cv2.GaussianBlur(flipped, (5, 5), 0)
        ret, th = cv2.threshold(
            blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        cv2.imwrite(path_template_sp1.format(0), th)
        return cv2.matchTemplate(washed_img, th, g_match_alg)

        # return cv2.matchTemplate(washed_img, self.templ_image, g_match_alg)


class Flow:
    def __init__(self, cb_resolution, cb_distance, cb_wash, cb_compare):
        self.cb_resolution = cb_resolution
        self.cb_distance = cb_distance
        self.cb_wash = cb_wash
        self.cb_compare = cb_compare
    
    def execute_resolution(self, high_constrast, img_color):
        return self.cb_resolution(high_constrast, img_color)
    
    def execute_distance(self):
        return self.cb_distance()
    
    def execute_wash(self, ready_img):
        return self.cb_wash(ready_img)

    def execute_compare(self, img_input, washed_image, suits, numbers):
        return self.cb_compare(img_input, washed_image, suits, numbers)
    