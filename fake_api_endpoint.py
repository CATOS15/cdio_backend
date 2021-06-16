from ml_solitaire.yolov5v2.result import map_img_cards
import cv2
import ml_solitaire.cut_image as ml_sol
import communication_layer.ml_alg as comm
import image_processing.g_shared as g_shared
import image_processing.flows as flows
import image_processing.img_recognition as imp


path_cut_tableau = "images/tmp/cut_tableau/col_{}.png"
path_cut_three = "images/tmp/cut_in_three/cut_{}.png"

#TODO
#Order cards in sequential columns
#Reevaluate tableau
#Create first flow for foundation

# 0 = waste, 1 = foundation, 2 = tableau
def opencv_solution(image_from_api):
    solitaire_split = flows.flow_ml_subdivide_tableau.cb_img_cut(image_from_api)
    # waste_results = imp.opencv_flow_waste(solitaire_split[0])
    # foundation_results = imp.opencv_flow_tableau(solitaire_split[1])
    tableau_results = imp.opencv_flow_tableau(solitaire_split[2])
    return (None, None, tableau_results)


def ml_solution(image_from_api):
    # split image into three
    solitaire_split = flows.flow_ml_subdivide_tableau.cb_img_cut(image_from_api)
    _test_cut_three(solitaire_split)

    # cuts columns
    # tableau = flows.flow_ml_subdivide_tableau.cb_cut_columns(solitaire_split[2])
    tableau = map_img_cards(solitaire_split[2]) #probably gives bad results
    waste = map_img_cards(solitaire_split[0])
    foundation = map_img_cards(solitaire_split[1])

    for i, img in enumerate(tableau):
        cv2.imwrite(path_cut_tableau.format(str(i)), img)
    

    # #mapping to algorithm
    # solitaire = {comm.ImageCardType.Waste: solitaire_split[0], comm.ImageCardType.Foundation: solitaire_split[1], comm.ImageCardType.Tableau: tableau}
    return (waste, foundation, tableau)
    # return flows.flow_ml_subdivide_tableau.cb_ml_execute(solitaire)

def opencv_run():
    return None


def _test_cut_three(solitaire_split):
    cv2.imwrite(path_cut_three.format("0"), solitaire_split[0])
    cv2.imwrite(path_cut_three.format("1"), solitaire_split[1])
    cv2.imwrite(path_cut_three.format("2"), solitaire_split[2])


def api_endpoint():
    # test_img = cv2.imread(g_shared.path_card_full_solitaire_red_background_distinct, cv2.IMREAD_COLOR)
    # call opencv and receive card object (image_processing/objects.py)
    test_img = cv2.imread(g_shared.path_card_full_solitaire_red_background, cv2.IMREAD_COLOR)
    
    cv_results = opencv_solution(test_img)
    for x in cv_results[2]:
        print(x)

    # call ml and receive card object (image_processing/objects.py)
    # ml_results = ml_solution(test_img)
    # for x in ml_results[2]:
    #     print(x)

    # remake object to algorithm objects
    # call algo



api_endpoint()
