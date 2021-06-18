import math

def cut_img_cut_three(img):
    #dimensions for image
    height = img.shape[0]
    width = img.shape[1]
    heightratio = 1/3 #hvor meget plads der er i toppen af linjegrided

    #cropped image *zones
    left_width = math.floor(width*2/5)
    top_height = math.floor(height*heightratio)

    #cropped images
    drawpile = img[0:top_height, 0:left_width]
    fountain = img[0:top_height, left_width:width]
    piles = img[top_height:height, 0:width]

    return (drawpile, fountain, piles)

