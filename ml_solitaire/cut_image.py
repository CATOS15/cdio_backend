import cv2
import numpy as np
import math

# read image
path_image = 'ml_solitaire\solitaire_ex1.jpg' #hav projektet åbent i CDIO_BACKEND som hoved folder
img = cv2.imread(path_image)

#dimensions for image
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
heightratio = 1/3 #hvor meget plads der er i toppen af linjegrided

def cut_and_save_images():
    #cropped image *zones
    left_width = math.floor(width*2/5)
    top_height = math.floor(height*heightratio)

    #cropped images
    drawpile = img[0:top_height, 0:left_width]
    fountain = img[0:top_height, left_width:width]
    piles = img[top_height:height, 0:width]

    #save images
    cv2.imwrite('ml_solitaire\image_drawpile.jpg', drawpile)
    cv2.imwrite('ml_solitaire\image_fountain.jpg', fountain)
    cv2.imwrite('ml_solitaire\image_piles.jpg', piles)

    """ cv2.imshow("cropped", drawpile)
    cv2.waitKey(0)

    cv2.imshow("cropped", fountain)
    cv2.waitKey(0)

    cv2.imshow("cropped", piles)
    cv2.waitKey(0)
    return """

""" def save_images():
    cv2.imwrite('image_drawpile.jpg', drawpile)
    cv2.imwrite('image_fountain.jpg', fountain)
    cv2.imwrite('image_piles.jpg', piles) """

def print_image_info():
    print(img.shape)
    # get dimensions of image
    dimensions = img.shape
    
    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    print('Image Dimension    : ',dimensions)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)

def cut_7_images():
    #cropped image *zones
    top_height = math.floor(height*1/3)

    #cropped images
    column1 = img[top_height:height, 0:math.floor(width*1/7)]
    column2 = img[top_height:height, math.floor(width*1/7):math.floor(width*2/7)]
    column3 = img[top_height:height, math.floor(width*2/7):math.floor(width*3/7)]
    column4 = img[top_height:height, math.floor(width*3/7):math.floor(width*4/7)]
    column5 = img[top_height:height, math.floor(width*4/7):math.floor(width*5/7)]
    column6 = img[top_height:height, math.floor(width*5/7):math.floor(width*6/7)]
    column7 = img[top_height:height, math.floor(width*6/7):width]

    #save images
    cv2.imwrite('ml_solitaire\image_column1.jpg', column1)
    cv2.imwrite('ml_solitaire\image_column2.jpg', column2)
    cv2.imwrite('ml_solitaire\image_column3.jpg', column3)
    cv2.imwrite('ml_solitaire\image_column4.jpg', column4)
    cv2.imwrite('ml_solitaire\image_column5.jpg', column5)
    cv2.imwrite('ml_solitaire\image_column6.jpg', column6)
    cv2.imwrite('ml_solitaire\image_column7.jpg', column7)

def show_cut_images():
    drawpile_path = 'ml_solitaire\image_drawpile.jpg'
    fountain_path = 'ml_solitaire\image_fountain.jpg'
    piles_path = 'ml_solitaire\image_piles.jpg'

    image_drawpile = cv2.imread(drawpile_path)
    image_fountain = cv2.imread(fountain_path)
    image_piles = cv2.imread(piles_path)

    cv2.imshow("cropped", image_drawpile)
    cv2.waitKey(0)

    cv2.imshow("cropped", image_fountain)
    cv2.waitKey(0)

    cv2.imshow("cropped", image_piles)
    cv2.waitKey(0)

cut_and_save_images()
cut_7_images()
show_cut_images()