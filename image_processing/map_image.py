import cv2
import numpy as np
from g_img import *

def locate_figure(img_color, img_grey, templ):
    matches = templ.compare_template(img_grey)
    loc = np.where(matches >= templ.threshold)    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(
            img_color, pt, (pt[0] + templ.width, pt[1] + templ.height), templ.drawSquare.color, templ.drawSquare.thicc)
    return img_color


def set_resolution(img_from, img_ideal):
    img_from_res = img_from.shape[0] * img_from.shape[1]
    img_ideal_res = img_ideal.shape[0] * img_ideal.shape[1]

    # same resolution
    if img_from_res - img_ideal_res == 0:
        return img_from
    # scale from to match ideal
    scale_height = img_ideal.shape[0] / img_from.shape[0]
    scale_width = img_ideal.shape[1] / img_from.shape[1]
    new_height = int(img_from.shape[0] * scale_height)
    new_width = int(img_from.shape[1] * scale_width)

    # decide on an algo
    return cv2.resize(img_from, (new_width, new_height))


def change_contour(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# require certain img format

# crazy expectations
    # ratio (delay)
    # rotate image

# Must have same resolution for template match (DONE)

# Set Contrast really high <-- countors archieved


# Compare Template w. img
 # TM_COEFF


# Different angles


# Consider blur (delay)
