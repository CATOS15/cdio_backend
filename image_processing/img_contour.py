import cv2
import numpy as np

def contours_sample1(img_thresh, alg1, alg2):
    contours, hierachy = cv2.findContours(
        img_thresh, alg1, alg2)
    img_cunts = [] 
    cuntour_area_req = 50000
    # contours
    for cunt in contours:
        if cv2.contourArea(cunt) > cuntour_area_req:
            img_cunts.append(np.array(__contour_draw(img_thresh, cunt)))
    return img_cunts


def __contour_draw(adaptive_th, cunt):
    rect = cv2.minAreaRect(cunt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(adaptive_th, [box], 0, (0, 0, 255), 2)
    x, y, w, h = cv2.boundingRect(cunt)
    return adaptive_th[y:y + h, x:x + w]