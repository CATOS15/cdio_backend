import enum
from ml_solitaire.yolov5v2.result import map_img_cards
import cv2
import ml_solitaire.cut_image as ml_sol
import ml_solitaire.ml_img_recognition as ml_imp
import communication_layer.ml_alg as comm
import image_processing.g_shared as g_shared
import image_processing.flows as flows
import image_processing.img_recognition as imp
import image_processing.objects as obj
import image_processing.debugging as debugging
import image_processing.img_resolution as resolution
import image_processing.g_img as g_img


path_cut_tableau = "images/tmp/cut_tableau/col_{}.png"
path_cut_three = "images/tmp/cut_in_three/cut_{}.png"

#TODO
#Order cards in sequential columns
#Reevaluate tableau
#Create first flow for foundation

# 0 = waste, 1 = foundation, 2 = tableau
def opencv_solution(image_from_api):
    solitaire_split = flows.flow_ml_subdivide_tableau.cb_img_cut(image_from_api)
    # debugging.print_results(solitaire_split, g_shared.path_contours_sp4)
        # set to black/white and invert templates
    tmpl_bin_img = resolution.bin_invert_templates(g_img.g_templates)
    # error when making grey-templates for more than 1 tableau
    waste_results = imp.opencv_flow_waste(solitaire_split[0], tmpl_bin_img) 
    foundation_results = imp.opencv_flow_waste(solitaire_split[1], tmpl_bin_img)
    tableau_results = imp.opencv_flow_tableau(solitaire_split[2], tmpl_bin_img)
    return (waste_results, foundation_results, tableau_results)


def ml_solution(image_from_api):
    # Split input image in three
    solitaire_split = flows.flow_ml_subdivide_tableau.cb_img_cut(image_from_api)
    
    waste_results = ml_imp.ml_flow_waste(solitaire_split[0])
    foundation_results = ml_imp.ml_flow_foundation(solitaire_split[1])
    tableau_results = ml_imp.ml_flow_tableau(solitaire_split[2]) 

    print("-----waste:-----")
    for column in waste_results:
        print('[', end = '')
        for card in column:
            print(card)
        print(']')

    print("-----foundation:-----")
    for column in foundation_results:
        print('[', end = '')
        for card in column:
            print(card)
        print(']')

    print("-----tableau:-----")
    for column in tableau_results:
        print('[', end = '')
        for card in column:
            print(card)
        print(']')

    return (waste_results,foundation_results,tableau_results)


#compare ml and opencv and return best solution
def compare_solutions(opencv_solution, ml_solution, type):
    if type == comm.ImageCardType.Tableau:
        return None #not implemented yet
    else:
        cards = []
        for i, ml_card in enumerate(ml_solution):
            card = obj.Card(None, None, None, None)
            if opencv_solution[i].suit != ml_card.suit:
                if opencv_solution[i].suit_threshold > ml_card.suit_threshold:
                    card.suit = opencv_solution[i].suit
                else:
                    card.suit = ml_card.suit
            elif opencv_solution[i].rank != ml_card.rank:
                if opencv_solution[i].rank_threshold > ml_card.rank_threshold:
                    card.rank = ml_card.rank
            else:
                card = ml_card
            cards.append(card)
        return cards


def _test_cut_three(solitaire_split):
    cv2.imwrite(path_cut_three.format("0"), solitaire_split[0])
    cv2.imwrite(path_cut_three.format("1"), solitaire_split[1])
    cv2.imwrite(path_cut_three.format("2"), solitaire_split[2])


def api_endpoint():
    # test_img = cv2.imread(g_shared.path_card_full_solitaire_red_background_distinct, cv2.IMREAD_COLOR)
    # test_img = cv2.imread(g_shared.path_card_full_solitaire_red_background, cv2.IMREAD_COLOR)
    test_img = cv2.imread(g_shared.path_card_full_solitaire_black_background, cv2.IMREAD_COLOR)
    
    # call opencv and receive card object (image_processing/objects.py)
    cv_results = opencv_solution(test_img)
    for x in cv_results[2]:
        print(x)

    
    ml_solution(test_img)
    # call ml and receive card object (image_processing/objects.py)
    # ml_results = ml_solution(test_img)
    # for x in ml_results[2]:
    #     print(x)

    # remake object to algorithm objects
    # call algo



api_endpoint()
