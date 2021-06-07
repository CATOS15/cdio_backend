from numpy.core.fromnumeric import resize
from g_img import *
from g_shared import *
from img_wash import *
from img_compare import *
from img_resolution import *
from debugging import *
from img_cut_suit_rank import *
# import os
from pathlib import Path

# Paths for images received
path_card_tableau = 'image_processing/templates/test/full_deck/tableau.png'
path_card_foundation = 'image_processing/templates/test/full_deck/foundation.png'
path_card_waste = 'image_processing/templates/test/full_deck/waste.png'
path_card_waste2 = 'image_processing/templates/test/full_deck/waste2.png'
path_card_waste3 = 'image_processing/templates/test/full_deck/waste3.png'
path_card_waste4 = 'image_processing/templates/test/full_deck/waste4.png'
path_card_waste5 = 'image_processing/templates/test/full_deck/waste5.png'
path_card_high_res = 'image_processing/templates/test/full_deck/full_solitare_1_2.png'
path_card_ideal_4_spades = 'image_processing/templates/card/ideal_cards/4_spades.PNG'

# print(Path(os.getcwd(), path_card_waste))

# Read cards
card_tableau_color = cv2.imread(path_card_tableau, cv2.IMREAD_COLOR)
card_foundation_color = cv2.imread(path_card_foundation, cv2.IMREAD_COLOR)
card_waste_color = cv2.imread(path_card_waste, cv2.IMREAD_COLOR)
card_waste2_color = cv2.imread(path_card_waste2, cv2.IMREAD_COLOR)
card_waste3_color = cv2.imread(path_card_waste3, cv2.IMREAD_COLOR)
card_waste4_color = cv2.imread(path_card_waste4, cv2.IMREAD_COLOR)
card_waste5_color = cv2.imread(path_card_waste5, cv2.IMREAD_COLOR)
four_spades = cv2.imread(path_card_ideal_4_spades, cv2.IMREAD_COLOR)
high_res_color = cv2.imread(path_card_high_res)
test = card_waste_color


# Waste flow
# wash (done)
# contour (done)
# wash2 (done)

# cut appropriately suit and number
# recognize number
# recognize suit

flow_waste = Flow(cb_wash=otsu_wash, cb_contour=contour_approximation,
                  cb_cut_suit_rank=find_by_hierachy, cb_compare_by_template=compare_templates)
# find card outlines
flow_waste_washed = flow_waste.execute_wash(test, cv2.THRESH_BINARY)

# cut these outlines
flow_waste_countours = flow_waste.execute_contour(
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_waste_washed, img_color=test)

# cut suit and number
washed_images = []
for i, cunt in enumerate(flow_waste_countours):
    washed_images.append(flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

# cut out images
flow_waste_cut = flow_waste.execute_cut_suit_rank(
    washed_images, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# bin invert templates
bin_invert_templates(g_templates)


# foo = g_templates[0]
# print(foo.club)
# template match all images contours for rank and suit
positive_matches = []
for i, tmpl_card in enumerate(g_templates):
    cv2.imwrite(path_contours_sp4.format(i), tmpl_card.img)
    # print_results(tmpl_card.img, path_contours_sp4)
    for x in flow_waste.execute_compare_by_template(flow_waste_cut, tmpl_card):
        for j in x:
            if j != None and j != 0:
                print(x)
        # print("----------------")
    # flow_waste.execute_compare_by_template(flow_waste_cut,tmpl_card)

    # tmpl_bin_inv(tmpl_card.img, "_INV_" + str(tmpl_card.value))
    # if tmpl_card.img is None:
    #     print("FUCK: " + str(tmpl_card.type) + ":" + str(tmpl_card.value))


# template match for numbers

# cnt = 0
# for card in flow_waste_cut:
#     print_results_suits_numbers(card['suits_numbers'], path_contours_sp4, cnt)
#     # print_results_suits_numbers(card['face_cards'], path_contours_sp4, cnt)
#     cnt += 1

# cv2.imshow("flow waste washed", resize_image(flow_waste_washed))
# cv2.waitKey(0)


# TODO
# WASTE
    # Refactor / cleanup
    # Go through structure for waste
    # Create templates for all Rank & Suits


# Notes
    # GaussianBlur
    # find video for more details
    # Consider canny edge detection
    # Tableau
    # Contour approx - Convex Hull https://docs.opencv.org/master/dd/d49/tutorial_py_contour_features.html
    # img_compare
    # Figure out if each point is a sum of euclidian kernel (assumed for now)
    # otherwise is each point in euclidian gitter a compariason match or something third
