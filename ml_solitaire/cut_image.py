import cv2
import numpy as np
import math

# read image
path_image = 'cdio_backend\ml_solitaire\solitaire.jpg'
img = cv2.imread(path_image)

#dimensions for image
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]



def cut_and_save_images():
    #cropped image *zones
    left_width = math.floor(width*2/5)
    top_height = math.floor(height*1/3)

    #cropped images
    drawpile = img[0:top_height, 0:left_width]
    fountain = img[0:top_height, left_width:width]
    piles = img[top_height:height, 0:width]

    #save images
    cv2.imwrite('cdio_backend\ml_solitaire\image_drawpile.jpg', drawpile)
    cv2.imwrite('cdio_backend\ml_solitaire\image_fountain.jpg', fountain)
    cv2.imwrite('cdio_backend\ml_solitaire\image_piles.jpg', piles)

    """ cv2.imshow("cropped", drawpile)
    cv2.waitKey(0)

    cv2.imshow("cropped", fountain)
    cv2.waitKey(0)

    cv2.imshow("cropped", piles)
    cv2.waitKey(0)
    return """

def save_images():
    cv2.imwrite('cdio_backend\ml_solitaire\image_drawpile.jpg', drawpile)
    cv2.imwrite('cdio_backend\ml_solitaire\image_fountain.jpg', fountain)
    cv2.imwrite('cdio_backend\ml_solitaire\image_piles.jpg', piles)

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

def show_cut_images():
    drawpile_path = 'cdio_backend\ml_solitaire\solitaire.jpg'
    fountain_path = 'cdio_backend\ml_solitaire\image_fountain.jpg'
    piles_path = 'cdio_backend\ml_solitaire\image_piles.jpg'

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
show_cut_images()