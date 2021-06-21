import image_processing.objects as obj
import image_processing.g_img as g_img
import communication_layer.ml_alg as comm
import image_processing.img_recognition as imp
import ml_solitaire.ml_img_recognition as ml_imp
import image_processing.img_resolution as resolution

from image_processing.img_compare import compare
from ml_solitaire.yolov5v2.result import map_img_cards


# 0 = waste, 1 = foundation, 2 = tableau
def opencv_solution(img_fractions):
    inv_bin_templates = resolution.bin_invert_templates(g_img.g_templates)

    waste_results = imp.opencv_flow_waste(img_fractions[0], inv_bin_templates) 
    foundation_results = imp.opencv_flow_waste(img_fractions[1], inv_bin_templates)
    tableau_results = imp.opencv_flow_tableau(img_fractions[2], inv_bin_templates)
    return (waste_results, foundation_results, tableau_results)


def ml_solution(img_fractions):    
    # Card recogniztion on each fraction (waste, foundation and tableau)
    waste_results = ml_imp.ml_flow_waste(img_fractions[0])
    foundation_results = ml_imp.ml_flow_foundation(img_fractions[1])
    tableau_results = ml_imp.ml_flow_tableau(img_fractions[2]) 

    return (waste_results,foundation_results,tableau_results)


#compare ml and opencv and return best solution
def compare_solutions(opencv_solution, ml_solution, type):
    if type == comm.ImageCardType.Tableau:
        return ml_solution
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