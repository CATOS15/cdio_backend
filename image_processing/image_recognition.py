#I HAVE A SHITTY LINTER, DON'T JUDGE
from g_img import *
from map_image import *

# path_card_high_res = './image_processing/templates/test/3_diamonds_hearts_high_res.png'
path_card_high_res = './image_processing/templates/test/many_cards_bad_lighting_1.png'

high_res_color = cv2.imread(path_card_high_res)

img_input = set_resolution(high_res_color, g_img_color)

#img is inverted
img_grey = change_contour(img_input)

img3 = locate_figure(img_grey, img_grey, g_templ_objs['diamond'])

# heart, diamonds, number = match_template_suit(img_grey, g_match_alg)
# img1 = locate_figure(img_input, img_grey, g_templ_objs['heart'])
# img2 = locate_figure(img1, img_grey, g_templ_objs['diamond'])
# img3 = locate_figure(img2, img_grey, g_templ_objs['number'][Cards.Three])

cv2.imwrite(result_image, img3)


#TODO
# Refactor change_contour
# make clean cut between light(guassianBlur, blue) and contour(contourArea)
# method for inverting && considering lightning for an img
# Array instead of writing images
# make sure locate_figure works! 

#if everything else fails, go back to basics:
#     img_contour = cv2.drawContours(img_grey, contours, -1, (0, 255, 0), 4)        


