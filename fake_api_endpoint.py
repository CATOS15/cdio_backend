import cv2
import ml_solitaire.cut_image as ml_sol
import communication_layer.ml_alg as comm
import image_processing.g_shared as g_shared
import image_processing.flows as flows


path_cut_tableau = "images/tmp/cut_tableau/col_{}.png"
path_cut_three = "images/tmp/cut_in_three/cut_{}.png"

#0 = waste, 1 = foundation, 2 = tableau
def ml_opencv_cut_columns(image_from_api):    
    #split image into three
    solitaire_split = flows.flow_ml_subdivide_tableau.cb_img_cut(image_from_api)
    _test_cut_three(solitaire_split)
    
    #cuts columns
    tableau = flows.flow_ml_subdivide_tableau.cb_cut_columns(solitaire_split[2])

    for i,img in enumerate(tableau):
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
   
    foo = ml_opencv_cut_columns(test_img)
    print(foo)
    #call algo(foo)
    
api_endpoint()