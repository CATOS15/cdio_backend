import cv2
import numpy as np
import math
import imutils
from PIL import Image
#transform you cool image into an even cooler version in 720x720


# read image
# path_image = 'ml_solitaire\solitaire_ex1.jpg' #hav projektet åbent i CDIO_BACKEND som hoved folder
# img = cv2.imread(path_image)


def make_square(im, min_size=256, fill_color=(255, 255, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def transform_720(img):
    #dimensions for image
    image720 = cv2.imread(img)
    
    dimensions = image720.shape
    # height = image720.shape[0]
    # width = image720.shape[1]

    # r = 720.0 / image720.shape[1]
    # dim = (720, int(image720.shape[0] * r))
    
    img = imutils.resize(image720, width=720)    

    #resized = cv2.resize(image720, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite('ml_solitaire\pestgul.png', img)
    cv2.imshow("resized", img)
    cv2.waitKey(0)

#test_image = Image.open('ml_solitaire\image_drawpile.jpg')
#new_image = make_square(test_image)

#new_image.show()

transform_720('ml_solitaire\image_drawpile.jpg')
