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
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lower, upper = 170, 255
        
    ret, thresh = cv2.threshold(img_grey, lower, upper, 0)
    #consider alg's for choosing contour
    contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours_found = 0
    path_contours = "image_processing/templates/card/result/contour_res_squares_{}.png"

    #contours
    for cunt in contours:
        if cv2.contourArea(cunt) > 50000:
                rect = cv2.minAreaRect(cunt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(img_grey,[box],0,(0,0,255),2)
                x, y, w, h = cv2.boundingRect(cunt)
                ROI = img_grey[y:y + h, x:x + w]
                cv2.imwrite(path_contours.format(contours_found), ROI)
                contours_found += 1
    
    #lightning
    for i in range(contours_found):
        cunt = cv2.imread(path_contours.format(str(i)), cv2.CV_8UC1)
        # th = cv2.adaptiveThreshold(tmp_cunt, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        blur = cv2.GaussianBlur(cunt,(5,5),0)
        ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        dst = cv2.bitwise_not(th3)
        cv2.imwrite(path_contours.format(str(i)), dst)
    
#     img_contour = cv2.drawContours(cv2.imread(path_contours.format('1')), contours, -1, (0, 255, 0), 4)      
    #set back to default  
    return cv2.imread(path_contours.format("4"), 0)    
    






# require certain img format

# crazy expectations
    # ratio (delay)
    # rotate image

# Must have same resolution for template match (DONE)

# Contour
        #Find each card as an object
        # Set Contrast really high for each object (maybe)
        #Go through each object and look for Suit
        #Go through each object and look for Number
        



# Compare Template w. img
 # TM_COEFF


# Different angles


# Consider blur (delay)
