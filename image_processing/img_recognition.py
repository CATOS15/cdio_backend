from numpy.core.fromnumeric import resize
# from image_processing import objects
import image_processing.objects as objects
import image_processing.g_img as g_img
import image_processing.g_shared as g_shared
import image_processing.objects as objects
import image_processing.img_wash as wash
import image_processing.img_contour as contour
import image_processing.img_compare as compare
import image_processing.img_resolution as resolution
import image_processing.debugging as debugging
import image_processing.img_cut_suit_rank as cut_suit_rank
import cv2
# from pathlib import Path

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
card_waste2_color = cv2.imread(
    path_card_waste2, cv2.IMREAD_COLOR)  # unable to find suit
card_waste3_color = cv2.imread(path_card_waste3, cv2.IMREAD_COLOR) #error
card_waste4_color = cv2.imread(path_card_waste4, cv2.IMREAD_COLOR) #wrong rank, no suit
card_waste5_color = cv2.imread(path_card_waste5, cv2.IMREAD_COLOR) #no rank, no suit
high_res_color = cv2.imread(path_card_high_res,cv2.IMREAD_COLOR) #error
test = card_waste_color

# Waste flow
# wash 
# contour 
# wash2 
# cut appropriately suit and number
# recognize number
# recognize suit
flow_waste = objects.Flow(cb_wash=wash.otsu_wash, cb_contour=contour.contour_approximation,
                  cb_cut_suit_rank=cut_suit_rank.find_by_hierachy, cb_compare_by_template=compare.compare_ranksuit)
# find card outlines
flow_waste_washed = flow_waste.execute_wash(test, cv2.THRESH_BINARY)

# cut these outlines
flow_waste_countours = flow_waste.execute_contour(
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_waste_washed, img_color=test)

# cut suit and number
washed_images = []
for i, cunt in enumerate(flow_waste_countours):
    washed_images.append(flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

debugging.print_results(washed_images, g_shared.path_contours_sp2)

# cut out images
flow_waste_cut = flow_waste.execute_cut_suit_rank(
    washed_images, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

debugging.print_waste_cuts(flow_waste_cut)

# set to black/white and invert templates
resolution.bin_invert_templates(g_img.g_templates)

# uses all cards
# compares all contours of a card with all templates
# creates a card from best match & global threshold
results = []
for i, card in enumerate(flow_waste_cut):
    results.append(flow_waste.execute_compare_by_template(card, g_img.g_templates))


for x in results:
    print(x)

# template match for numbers


# cv2.imshow("flow waste washed", resize_image(flow_waste_washed))
# cv2.waitKey(0)


# TODO
# WASTE
    #Create Integration Test for Waste
        #Create unit test for each algo in Waste
    #consider folder structure
# Notes
    # GaussianBlur
    # find video for more details
    # Consider canny edge detection
    # Tableau
    # Contour approx - Convex Hull https://docs.opencv.org/master/dd/d49/tutorial_py_contour_features.html
    # img_compare
    # Figure out if each point is a sum of euclidian kernel (assumed for now)
    # otherwise is each point in euclidian gitter a compariason match or something third


# TODO Rapport
# Testing
    # Test different algorithms, and compare them together
    #
