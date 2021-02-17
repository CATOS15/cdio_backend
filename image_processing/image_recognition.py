import os
#g_img imports cv2 & numpy
from g_img import * 
from image_processing import locate_figure

number_success = locate_figure(number_match, g_threshold, w_number, h_number, g_red_square)
suit_success = locate_figure(suit_diamonds_match, g_threshold, w_suit_diamonds, h_suit_diamonds, g_green_square)
# locate_figure(suit_heart_match, g_threshold, w_suit_heart, h_suit_heart, g_blue_square)

cv2.imwrite(result_image, g_img_color)



