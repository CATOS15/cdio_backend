from g_img import *
from img_wash import *
from img_compare import *
from img_resolution import *
import os
from pathlib import Path

# Paths
path_card_tableau = 'image_processing\\templates\\test\\full_deck\\collumns_full_solitare.png'
path_card_foundation = 'image_processing/templates/test/full_deck/fountain_full_solitare.png'


path_card_high_res = 'image_processing/templates/test/full_deck/full_solitare_1_2.png' 
print(Path(os.getcwd(), path_card_waste))

# Read cards
card_tableau_color = cv2.imread(path_card_tableau)
card_foundation_color = cv2.imread(path_card_foundation)
card_waste_color = cv2.imread(path_card_waste, 0)
high_res_color = cv2.imread(path_card_high_res)


# Waste flow
#binary
#threshold
#contours
flow_waste = Flow(None, None, blob_wash, None, contours_sample1)
flow_waste_washed = flow_waste.execute_wash(card_waste_color, cv2.THRESH_BINARY)
flow_waste_countours = flow_waste.execute_contour(flow_waste_washed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i,cunt in enumerate(flow_waste_countours):
    cv2.imwrite(result_image_sp4.format("_contour", i), cunt)

#set resolution, split image, wash each, compare images
# flow_simple = Flow(ratio_img_resolution, None, wash_img, compare)
# flow_simple_img = flow_simple.execute_resolution(high_res_color, g_img_color)
# flow_simple_washed_images = flow_simple.execute_wash(flow_simple_img)
# flow_simple_res_suits, flow_simple_res_numbers = flow_simple.cb_compare(flow_simple_img, flow_simple_washed_images, g_suits, g_numbers)

# write_to(result_image_sp1, flow_simple_res_suits, flow_simple_res_numbers)

#cmp resized template and image.
# flow_two = Flow(ratio_img_resolution, None, wash_img, compare, contours_sample1)
# flow_two_img = flow_two.execute_resolution(high_res_color, g_img_ideal_color)
# flow_two_threshold = define_threshold(flow_two_img, g_lower_threshold, g_upper_threshold)

# flow_two_contours = flow_two.execute_contour(flow_two_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# flow_two_washed_images = flow_two.execute_wash(flow_two_img, flow_two_contours)
# avg_columns_width = avg_columns_width(flow_two_washed_images)

# resized_suits = ratio_template_resolution(g_suits, avg_columns_width,g_ideal_card_suit_width,g_ideal_card_suit_height)
# resized_numbers = ratio_template_resolution(g_numbers, avg_columns_width,g_ideal_card_number_width,g_ideal_card_number_height)
# res_suits, res_numbers = flow_two.cb_compare(flow_two_img, flow_two_washed_images, resized_suits, resized_numbers)

# write_to(result_image_sp2, res_suits, res_numbers)

#Next time
#flow_three = Flow(..)
# write_to(result_image_sp3, res_suits, res_numbers)



#TODO
#Make Contour work for a single solitaire 
    #Make contour work for a new, different solitaire
#research
    #Feature Detection 



