import image_processing.flows as flows
import image_processing.debugging as debugging
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
    waste_result = list(set(waste_cards))

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
    foundation_result = list(set(foundation_cards))

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
    s = set(tableau_cards)
    tableau_result = list(s)

    return tableau_result

