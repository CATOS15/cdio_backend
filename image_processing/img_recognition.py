from g_img import *
from img_wash import *
from img_compare import *
from img_resolution import *

#input
path_card_high_res = './image_processing/templates/test/full_solitare_1_2.png'
high_res_color = cv2.imread(path_card_high_res)


#set resolution, split image, wash each, compare images
# flow_simple = Flow(ratio_img_resolution, None, wash_img, compare)
# flow_simple_img = flow_simple.execute_resolution(high_res_color, g_img_color)
# flow_simple_washed_images = flow_simple.execute_wash(flow_simple_img)
# flow_simple_res_suits, flow_simple_res_numbers = flow_simple.cb_compare(flow_simple_img, flow_simple_washed_images, g_suits, g_numbers)

# write_to(result_image_sp1, flow_simple_res_suits, flow_simple_res_numbers)

#cmp resized template and image.
flow_two = Flow(ratio_img_resolution, None, wash_img, compare)
flow_two_img = flow_two.execute_resolution(high_res_color, g_img_ideal_color)
flow_two_washed_images = flow_two.execute_wash(flow_two_img)
avg_columns_width = avg_columns_width(flow_two_washed_images)

resized_suits = ratio_template_resolution(g_suits, avg_columns_width,g_ideal_card_suit_width,g_ideal_card_suit_height)
resized_numbers = ratio_template_resolution(g_numbers, avg_columns_width,g_ideal_card_number_width,g_ideal_card_number_height)
res_suits, res_numbers = flow_two.cb_compare(flow_two_img, flow_two_washed_images, resized_suits, resized_numbers)

write_to(result_image_sp2, res_suits, res_numbers)
# cv2.imshow("resized_suits",resized_suits[0].templ_image)
# cv2.imshow("resized_numbers",resized_numbers[0].templ_image)
# cv2.waitKey(0)

#TODO

#research
    #Feature Detection 



