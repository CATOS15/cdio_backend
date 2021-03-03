import cv2
import numpy as np
from g_img import *
# from PIL import Image

def print_img(img):
    return


def print_images(images):
    return

def store_images(images, path):
    for i, img in enumerate(images):
        cv2.imwrite(path.format(i), img)

#MORMORS MØRKERUM BITCH
def wash_img(img):
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lower, upper = 170, 255
    # lightning,
    
    #use threshold to identify patterns
    ret_sample1, thresh_sample1 =  cv2.threshold(img_grey, lower, upper, 0)
    #seperate all cards
    cunts_1_sample = __contours(thresh_sample1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    
    wash_split_img = []
    for img_sample1 in cunts_1_sample:
        # wash_split_img.append(__lighting(img_sample1, lower, upper))
        wash_split_img.append(img_sample1)
    #use OSTU to clear up noice from cards
    img_1_clear = __contrast_flip_images(wash_split_img, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    store_images(img_1_clear, path_contours_sp1)
    
    # store_images(img_1_clear, path_contours_sp1)
    # return wash_split_img
    return img_1_clear

    # store_images(img_1_clear, path_contours_sp1)
    
    # tmpl_ret, tmpl_thresh_sample1 = templ_threshold(__tmpl_heart, lower, upper)
    # tmpl_grey = cv2.cvtColor(g_suits[0].templ_image, cv2.COLOR_BGR2GRAY)
    # tmpl_threshold = cv2.adaptiveThreshold(tmpl_grey, upper, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, pixel_neighborhood, subtract_mean)
    # tmpl_washed = __contrast_flip_images(tmpl_threshold, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cv2.imwrite(path_template_sp1, tmpl_washed)
    # cv2.imwrite(path_template_sp1,tmpl_grey)

    # #sample2 - lightning, find contours, 
    # th_sample2 = __lighting(img_grey, lower, upper)
    # cunt_2_sample = __contours(th_sample2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # img2_sample = __clear_images(cunt_2_sample, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # store_images(img2_sample, path_contours_sp2)
    
    # #sample3
    # th_sample3 = __lighting(img_grey, lower, upper)
    # img_3_sample = __clear_image(th_sample3, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # cunt_3_sample = __contours(img_3_sample, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # store_images(cunt_3_sample, path_contours_sp3)

    # set back to default
    # return cv2.imread(path_contours.format("4"), 0)



def templ_threshold(templInfo, lower, upper):
    cv2.threshold(templInfo.templ_image, lower, upper, 0)



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


def __lighting(img, lower, upper):
    # ret, thresh = cv2.threshold(img_grey, lower, upper, 0)
    pixel_neighborhood = 11
    subtract_mean = 2
    return cv2.adaptiveThreshold(img, upper, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, pixel_neighborhood, subtract_mean)
    # return th


def __contours(img_thresh, alg1, alg2):
    contours, hierachy = cv2.findContours(
        img_thresh, alg1, alg2)
    img_cunts = []  # this is funny
    cuntour_area_req = 50000
    # contours
    for cunt in contours:
        if cv2.contourArea(cunt) > cuntour_area_req:
            img_cunts.append(np.array(__contour(img_thresh, cunt)))
            # cv2.imwrite(path_contours.format("_cuntour_3"), img_cunts[0])
    return img_cunts


def __contour(adaptive_th, cunt):
    rect = cv2.minAreaRect(cunt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(adaptive_th, [box], 0, (0, 0, 255), 2)
    x, y, w, h = cv2.boundingRect(cunt)
    return adaptive_th[y:y + h, x:x + w]


def __clear_image(img, alg1):
    # define array
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv2.threshold(
        img, 0, 255, alg1)

    dst = cv2.bitwise_not(th3)
    # cv2.imwrite(store_path, th3)
    return dst


def __contrast_flip_images(img_cunts, alg1):
    imgs = []
    for i, cunt in enumerate(img_cunts):
        blur = cv2.GaussianBlur(cunt, (5, 5), 0)
        ret3, th3 = cv2.threshold(
            blur, 0, 255, alg1)
        # dst = cv2.bitwise_not(th3)
        # imgs.append(th3)
        imgs.append(th3)
        # cv2.imwrite(path_contours_sp2.format(str(i)), dst)
    return imgs


# require certain img format

# crazy expectations
    # ratio (delay)
    # rotate image

# Must have same resolution for template match (DONE)

# Contour
    # Find each card as an object
    # Set Contrast really high for each object (maybe)
    # Go through each object and look for Suit
    # Go through each object and look for Number


# Compare Template w. img
 # TM_COEFF


# Different angles


# Consider blur (delay)
