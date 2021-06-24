#Gruppe 15
#Christian Frost s184140
#Mikkel Lindtner s205421 
#Nikolai Stein s205469
#Oliver Christensen s176352
#Søren Andersen s182881
#Tobias Kristensen s195458

import image_processing.flows as flows
import ml_solitaire.transform720 as tf720
from ml_solitaire.yolov5v2.result import map_img_cards


def ml_flow_waste(waste_color_img):
    # Start with waste
    columns_color_waste = flows.flow_ml_subdivide_tableau.cb_cut_columns(waste_color_img)

    # Waste set 720x720_res
    columns_color_waste_res720 = []
    for image in columns_color_waste:
        columns_color_waste_res720.append(tf720.transform_720(image))

    # Find cards and map  
    waste_cards = []
    for image in columns_color_waste_res720:
        waste_cards.append(map_img_cards(image))

    # Check for duplicate
    waste_no_duplicates = remove_duplicates(waste_cards)

    # Sort cards
    waste_result = sort_cards(waste_no_duplicates)

    return waste_result


def ml_flow_foundation(foundation_color_img):
    # Start with waste
    columns_color_foundation = flows.flow_ml_subdivide_tableau.cb_cut_columns(foundation_color_img)

    # Waste set 720x720_res
    columns_color_foundation_res720 = []
    for image in columns_color_foundation:
        columns_color_foundation_res720.append(tf720.transform_720(image))

    # Find cards and map    
    foundation_cards = []
    for image in columns_color_foundation_res720:
        foundation_cards.append(map_img_cards(image))

    # Check for duplicate
    foundation_no_duplicates = remove_duplicates(foundation_cards)

    # Sort cards
    foundation_result = sort_cards(foundation_no_duplicates)

    return foundation_result


def ml_flow_tableau(tableau_color_img):
    # Start with waste
    columns_color_tableau = flows.flow_ml_subdivide_tableau.cb_cut_columns(tableau_color_img)

    # Waste set 720x720_res
    columns_color_tableau_res720 = []
    for image in columns_color_tableau:
        columns_color_tableau_res720.append(tf720.transform_720(image))

    # Find cards and map    
    tableau_cards = []
    for image in columns_color_tableau_res720:
       tableau_cards.append(map_img_cards(image))

    # Check for duplicate
    tableau_no_duplicates = remove_duplicates(tableau_cards)

    # Sort cards
    tableau_result = sort_cards(tableau_no_duplicates)

    return tableau_result



def remove_duplicates(cards):
    card_result = []

    for column in cards:
        card_result.append(list(set(column)))

    return card_result


def sort_cards(cards):
    card_result = []

    for column in cards:
        card_result.append(sorted(column, key=lambda x: x.rank.value, reverse=True))

    return card_result




