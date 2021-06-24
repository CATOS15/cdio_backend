#Gruppe 15
#Christian Frost s184140
#Mikkel Lindtner s205421 
#Nikolai Stein s205469
#Oliver Christensen s176352
#Søren Andersen s182881
#Tobias Kristensen s195458

import cv2
import image_processing.flows as flows

from numpy.core.fromnumeric import resize


def opencv_flow_waste(waste_color_image, tmpl_bin_img):
    # find card outlines
    washed_img = flows.flow_waste.execute_wash(waste_color_image, cv2.THRESH_BINARY)

    # cut these outlines
    countours = flows.flow_waste.execute_contour(
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=washed_img, img_color=waste_color_image)

    # cut suit and number
    cunt_images = []
    for i, cunt in enumerate(countours):
        cunt_images.append(flows.flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

    # cut out images
    suits_ranks = flows.flow_waste.execute_cut_suit_rank(
        cunt_images, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # compares all contours of a card with all templates
    # creates a card from best match & global threshold
    results = []
    for card in suits_ranks:
        results.append(flows.flow_waste.execute_compare_by_template(card, tmpl_bin_img))
    return results


def opencv_flow_tableau(tableau_color_img, tmpl_bin_img):
    flow_tableau_washed = flows.opencv_flow_tableau.execute_wash(tableau_color_img, cv2.THRESH_BINARY)

    # cut these outlines
    flow_tableau_countours = flows.opencv_flow_tableau.execute_contour(
        alg1=cv2.RETR_EXTERNAL, alg2=cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_tableau_washed, img_color=tableau_color_img)

    washed_images = []
    for i, cunt in enumerate(flow_tableau_countours):
        washed_images.append(flows.flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

    flow_tableau_cut = flows.opencv_flow_tableau.execute_cut_suit_rank(
        washed_images, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    results = []
    for i, card in enumerate(flow_tableau_cut):
        results.append(flows.opencv_flow_tableau.execute_compare_by_template(card, tmpl_bin_img))
    return results