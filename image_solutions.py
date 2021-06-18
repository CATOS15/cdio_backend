import enum
from image_processing.img_compare import compare
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
import json
import algorithm.image_algorithm as alg


path_cut_tableau = "images/tmp/cut_tableau/col_{}.png"
path_cut_three = "images/tmp/cut_in_three/cut_{}.png"

#TODO
#Order cards in sequential columns
#Reevaluate tableau
#Create first flow for foundation

# 0 = waste, 1 = foundation, 2 = tableau
def opencv_solution(solitaire_split):
    tmpl_bin_img = resolution.bin_invert_templates(g_img.g_templates)

    waste_results = imp.opencv_flow_waste(solitaire_split[0], tmpl_bin_img) 
    foundation_results = imp.opencv_flow_waste(solitaire_split[1], tmpl_bin_img)
    tableau_results = imp.opencv_flow_tableau(solitaire_split[2], tmpl_bin_img)
    return (waste_results, foundation_results, tableau_results)


def ml_solution(solitaire_split):    
    # Card recogniztion on each fraction (waste, foundation and tableau)
    waste_results = ml_imp.ml_flow_waste(solitaire_split[0])
    foundation_results = ml_imp.ml_flow_foundation(solitaire_split[1])
    tableau_results = ml_imp.ml_flow_tableau(solitaire_split[2]) 

    return (waste_results,foundation_results,tableau_results)


#compare ml and opencv and return best solution
def compare_solutions(opencv_solution, ml_solution, type):
    if type == comm.ImageCardType.Tableau:
        return ml_solution
        # return None #not implemented yet
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



# def api_endpoint():
#     # test_img = cv2.imread(g_shared.path_card_full_solitaire_red_background_distinct, cv2.IMREAD_COLOR)
#     # test_img = cv2.imread(g_shared.path_card_full_solitaire_red_background, cv2.IMREAD_COLOR)
#     test_img = cv2.imread(g_shared.path_card_full_solitaire_black_clean_background, cv2.IMREAD_COLOR)
    
#     # call opencv and receive card object (image_processing/objects.py)
#     cv_results = opencv_solution(test_img)
#     # for x in cv_results[2]:
#     #     print(x)

    

#     # call ml and receive card object (image_processing/objects.py)
#     ml_results = ml_solution(test_img)
#     # for x in ml_results[2]:
#     #     print(x)
    
#     # best_waste = compare_solutions(cv_results[0], ml_results[0], comm.ImageCardType.Waste)
#     # best_foundation = compare_solutions(cv_results[1], ml_results[1], comm.ImageCardType.Foundation)
#     # best_tableau = compare_solutions(cv_results[2], ml_results[2], comm.ImageCardType.Tableau)
#     solitaire_alg = {}
    
#     solitaire_alg['waste'] = comm.map_opencv_alg(cv_results[0], comm.ImageCardType.Waste)
#     solitaire_alg['fountains'] = comm.map_opencv_alg(cv_results[1], comm.ImageCardType.Foundation)
#     solitaire_alg['tableau'] = comm.map_opencv_alg(ml_results[2], comm.ImageCardType.Tableau)
    
#     # solitaire_json = json.dumps(solitaire_alg)
#     # print(alg.run_algorithm(solitaire_json))
#     bestmove = alg.run_algorithm(solitaire_alg)
#     print(bestmove["move"].description)


# api_endpoint()
