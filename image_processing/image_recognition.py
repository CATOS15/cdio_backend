#I HAVE A SHITTY LINTER, DON'T JUDGE
from g_img import *
from map_image import *

path_card_high_res = './image_processing/templates/test/3_diamonds_hearts_high_res.png'
high_res_color = cv2.imread(path_card_high_res)

img_input = set_resolution(high_res_color, g_img_color)

img_grey = change_contour(img_input)

# heart, diamonds, number = match_template_suit(img_grey, g_match_alg)
img1 = locate_figure(img_input, img_grey, g_templ_objs['heart'])
img2 = locate_figure(img1, img_grey, g_templ_objs['diamond'])
img3 = locate_figure(img2, img_grey, g_templ_objs['number'][Cards.Three])

cv2.imwrite(result_image, img3)
