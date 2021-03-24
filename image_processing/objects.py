import cv2
from g_shared import *


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
