#Gruppe 15
#Christian Frost s184140
#Mikkel Lindtner s205421 
#Nikolai Stein s205469
#Oliver Christensen s176352
#Søren Andersen s182881
#Tobias Kristensen s195458

import math

def cut_img_cut_three(img):
    #dimensions for image
    height = img.shape[0]
    width = img.shape[1]
    # heightratio = 7/24 #hvor meget plads der er i toppen af linjegrided
    heightratio = 1/3 #hvor meget plads der er i toppen af linjegrided

    #cropped image *zones
    left_width = math.floor(width*2/5)
    top_height = math.floor(height*heightratio)

    #cropped images
    waste = img[0:top_height, 0:left_width]
    foundation = img[0:top_height, left_width:width]
    tableau = img[top_height:height, 0:width]

    return (waste, foundation, tableau)

