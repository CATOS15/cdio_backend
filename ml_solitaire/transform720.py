#transform you cool image into an even cooler version in 720x720 with a yellow background
import cv2
import numpy as np
import math
#import imutils

# path_image = 'ml_solitaire\solitaire_ex1.jpg'
# img = cv2.imread(path_image)

def transform_720(img):
    #dimensions for image
    image720 = img
    height = image720.shape[0]
    width = image720.shape[1]

    #yellow square image
    yellow_square_path = 'ml_solitaire/yellow_square.png'
    yellow_square = cv2.imread(yellow_square_path)
    bg_height = yellow_square.shape[0]
    bg_width = yellow_square.shape[1]

    #gør input 720 bredde eller højde
    #allerede firkantet
    if(height==width):
        dimensioner = (720, 720)
        scaledimg = cv2.resize(image720, dimensioner, interpolation = cv2.INTER_AREA)

    #højt
    elif(height > width):
        scale = 720/height
        dimensioner = (math.floor(width*scale), 720)
        scaledimg = cv2.resize(image720, dimensioner, interpolation = cv2.INTER_AREA)
        
    #bredt
    elif(height < width):
        scale = 720/width
        dimensioner = (720, math.floor(height*scale))
        scaledimg = cv2.resize(image720, dimensioner, interpolation = cv2.INTER_AREA)

    #giv det en background
    #ligger det skalerede billede oveni det andet billede med et offset så det er i midten

    img = scaledimg
    s_height, s_width, lort = scaledimg.shape

    yoff = round((bg_height-s_height)/2)
    xoff = round((bg_width-s_width)/2)

    result = yellow_square.copy()
    result[yoff:yoff+s_height, xoff:xoff+s_width] = scaledimg

    # cv2.imwrite('ml_solitaire\pestgul.png', scaledimg)
    # cv2.imshow("resized", scaledimg)
    # cv2.waitKey(0)

    # cv2.imshow('CENTERED', result)
    # cv2.waitKey(0)
    
    return result

#transformed = transform_720('ml_solitaire\image_fountain.jpg')
#cv2.imshow("resized", transformed)
#cv2.waitKey(0)

