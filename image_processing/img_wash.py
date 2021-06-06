import cv2
import numpy as np
from g_img import *
from img_contour import *

def store_images(images, path):
    for i, img in enumerate(images):
        cv2.imwrite(path.format(i), img)

# MORMORS MØRKERUM BITCH'ÈS
def wash_img(img, cunts_1_sample):
    wash_split_img = []
    for img_sample1 in cunts_1_sample:
        wash_split_img.append(img_sample1)

    # use OSTU to clear up noice from cards
    img_1_clear = __contrast_flip_images(
        wash_split_img, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    store_images(img_1_clear, path_contours_sp2)

    return img_1_clear



# def wash_img_sample2():
#     th_sample2 = __lighting(img_grey, lower, upper)
#     cunt_2_sample = __contours(
#         th_sample2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     img2_sample = __clear_images(
#         cunt_2_sample, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#     store_images(img2_sample, path_contours_sp2)


# def wash_img_sample3():
#     th_sample3 = __lighting(img_grey, lower, upper)
#     img_3_sample = __clear_image(th_sample3, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#     cunt_3_sample = __contours(
#         img_3_sample, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     store_images(cunt_3_sample, path_contours_sp3)


def templ_threshold(templInfo, lower, upper):
    cv2.threshold(templInfo.templ_image, lower, upper, 0)


def __lighting(img, lower, upper):
    # ret, thresh = cv2.threshold(img_grey, lower, upper, 0)
    pixel_neighborhood = 11
    subtract_mean = 2
    return cv2.adaptiveThreshold(img, upper, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, pixel_neighborhood, subtract_mean)
    # return th

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


def adaptive_wash(image, alg1):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gaus_kernel_size = (5,5)
    blur = cv2.GaussianBlur(gray,gaus_kernel_size,0)
    # adaptive_threshold = 60
    block_size = 13 #dependant on resolution
    C = 3 #dependant on on resolution used together with blocksize
    white = 255
    
    #adapt to lightning
    thresh = cv2.adaptiveThreshold(blur, white, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, alg1, block_size, C)

    return thresh

def otsu_wash(image, alg1):
    black = 0
    white = 255
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (1,1), 0)
    _, th3 = cv2.threshold(blur, black, white, alg1+cv2.THRESH_OTSU)
    return th3 



