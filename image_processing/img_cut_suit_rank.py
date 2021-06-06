import cv2
import numpy as np
from img_contour import __contour_draw

def find_by_hierachy(contours, alg1, alg2):
    relevant = []

    card = contours[0] 
    countours, hierachy = cv2.findContours(card, alg1, alg2)     
    hierachy_area = 45000 / 2

    # foo = contours[hierachy[0][2]].next
    foo = hierachy[0][0][0]
    foo1 = hierachy[0][0][1]
    foo2 = hierachy[0][0][2]
    foo3 = hierachy[0][0][3]
    foo4 = hierachy[0][1][3]
    # foo = hierachy[1][0][0]


    for i,cunt in enumerate(countours):
        #for some unholy reason there is a 3rd diemension, may god save the man who inveted this soul, course I wont 
        if hierachy[0][i][3] == 0:             
            relevant.append(np.array(__contour_draw(card, cunt))) #find a way to draw contours 
    return relevant 
    # for cunt in contours:
    #     contours, hierachy = cv2.findContours(cunt, alg1, alg2)
        