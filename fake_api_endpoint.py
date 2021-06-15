import cv2
import ml_solitaire.cut_image as ml_sol
import communication_layer.ml_alg as comm
import image_processing.g_shared as g_shared
import image_processing.flows as flows
import image_processing.img_recognition as imp


path_cut_tableau = "images/tmp/cut_tableau/col_{}.png"
path_cut_three = "images/tmp/cut_in_three/cut_{}.png"


def opencv_solution(image_from_api):
    solitaire_split = flows.flow_ml_subdivide_tableau.cb_img_cut(image_from_api)
    # get each card from tableau (later)
    # get each card from foundation (later)
    # get each card from waste
    cards_opencv = imp.opencv_flow_waste(solitaire_split[0])
    return cards_opencv
   
    # return best bet as card
    # return None
    # 0 = waste, 1 = foundation, 2 = tableau


def ml_opencv_cut_columns(image_from_api):
    # split image into three
    solitaire_split = flows.flow_ml_subdivide_tableau.cb_img_cut(image_from_api)
    _test_cut_three(solitaire_split)

    # cuts columns
    tableau = flows.flow_ml_subdivide_tableau.cb_cut_columns(solitaire_split[2])

    for i, img in enumerate(tableau):
        cv2.imwrite(path_cut_tableau.format(str(i)), img)

    # #mapping to algorithm
    solitaire = {comm.ImageCardType.Waste: solitaire_split[0], comm.ImageCardType.Foundation: solitaire_split[1], comm.ImageCardType.Tableau: tableau}
    return flows.flow_ml_subdivide_tableau.cb_ml_execute(solitaire)


def opencv_run():
    return None


def _test_cut_three(solitaire_split):
    cv2.imwrite(path_cut_three.format("0"), solitaire_split[0])
    cv2.imwrite(path_cut_three.format("1"), solitaire_split[1])
    cv2.imwrite(path_cut_three.format("2"), solitaire_split[2])


def api_endpoint():
    test_img = cv2.imread(g_shared.path_card_full_solitaire_red_background, cv2.IMREAD_COLOR)
    # call flow and receive card object (image_processing/objects.py)
    cv_results = opencv_solution(test_img)

    # call ml and receive card object (image_processing/objects.py)
    # ml_results = ml_solution(test_img)
    
    
    # compare best result
    
    
    # foo = ml_opencv_cut_columns(test_img)
    # print(foo)
    # call algo(foo)

api_endpoint()
