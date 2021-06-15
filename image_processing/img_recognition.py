import cv2
from numpy.core.fromnumeric import resize
import image_processing.g_img as g_img
import image_processing.g_shared as g_shared
import image_processing.img_resolution as resolution
import image_processing.debugging as debugging
import image_processing.flows as flows


def opencv_flow_waste(waste_color_image):
    # find card outlines
    flow_waste_washed = flows.flow_waste.execute_wash(waste_color_image, cv2.THRESH_BINARY)
    # flow_waste_washed = flows.flow_waste.execute_wash(g_shared.test, cv2.THRESH_BINARY) #works

    # cut these outlines
    flow_waste_countours = flows.flow_waste.execute_contour(
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_waste_washed, img_color=waste_color_image)

    # cut suit and number
    washed_images = []
    for i, cunt in enumerate(flow_waste_countours):
        washed_images.append(flows.flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

    # debugging.print_results(washed_images, g_shared.path_contours_sp2)

    # cut out images
    flow_waste_cut = flows.flow_waste.execute_cut_suit_rank(
        washed_images, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # debugging.print_waste_cuts(flow_waste_cut)

    # set to black/white and invert templates
    tmpl_bin_img = resolution.bin_invert_templates(g_img.g_templates)

    # uses all cards
    # compares all contours of a card with all templates
    # creates a card from best match & global threshold
    results = []
    for i, card in enumerate(flow_waste_cut):
        results.append(flows.flow_waste.execute_compare_by_template(card, tmpl_bin_img))
    return results


def opencv_flow_tableau(tableau_color_img):
    flow_tableau_washed = flows.opencv_flow_tableau.execute_wash(tableau_color_img, cv2.THRESH_BINARY)

    # cut these outlines
    flow_tableau_countours = flows.opencv_flow_tableau.execute_contour(
        alg1=cv2.RETR_EXTERNAL, alg2=cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_tableau_washed, img_color=tableau_color_img)

    debugging.print_results(flow_tableau_countours, g_shared.path_contours_sp1)
    washed_images = []
    for i, cunt in enumerate(flow_tableau_countours):
        washed_images.append(flows.flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

    debugging.print_results(washed_images, g_shared.path_contours_sp2)

    tmpl_bin_img = resolution.bin_invert_templates(g_img.g_templates)

    flow_tableau_cut = flows.opencv_flow_tableau.execute_cut_suit_rank(
        washed_images, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # debugging.print_waste_cuts(flow_tableau_cut)

    results = []
    for i, card in enumerate(flow_tableau_cut):
        results.append(flows.opencv_flow_tableau.execute_compare_by_template(card, tmpl_bin_img))
    return results



# Waste flow
    # wash
    # contour
    # wash2
    # cut appropriately suit and number
    # recognize number
    # recognize suit

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


#notes - code
# cv2.imshow("flow waste washed", resize_image(flow_waste_washed))
# cv2.waitKey(0)
# print(Path(os.getcwd(), path_card_waste))
