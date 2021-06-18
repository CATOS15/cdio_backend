import cv2
import math

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
    if((height < 720) and (width < 720)):
        scaledimg = image720
    
    elif(height==width):
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


    img = scaledimg
    s_height, s_width, lort = scaledimg.shape

    yoff = round((bg_height-s_height)/2)
    xoff = round((bg_width-s_width)/2)

    result = yellow_square.copy()
    result[yoff:yoff+s_height, xoff:xoff+s_width] = scaledimg
    return cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

