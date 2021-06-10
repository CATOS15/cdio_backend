import communication_layer.ml_alg as comm
import ml_solitaire.cut_image as ml_sol


def ml_opencv_cut_columns(image_from_api):    
    solitaire_split = ml_sol.cut_image.cut_image_in_three(image_from_api)
    tableau = comm.opencv_ml_tableau_columns_color(solitaire_split[2])
    fooz = {solitaire_split[0]: comm.ImageCardType.Waste, solitaire_split[1]: comm.ImageCardType.Foundation, tableau: comm.ImageCardType.Tableau}
    return comm.ml_map_alg(fooz)


def opencv_run():
    return None



def api_endpoint():    
    #correlation comparison for ml vs opencv
        #consider which correlation to use
    #compare correlations  