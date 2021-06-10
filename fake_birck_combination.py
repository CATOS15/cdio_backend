import communication_layer.ml_alg as comm



def ml_opencv_columns_run():
    foo = None  # cut image and receive in 3
    waste = comm.opencv_ml_tableau_columns_color(foo[0])
    foundation = comm.opencv_ml_tableau_columns_color(foo[1])
    tableau = comm.opencv_ml_tableau_columns_color(foo[2])
    
    fooz = {waste: comm.ImageCardType.Waste, foundation: comm.ImageCardType.Foundation, tableau: comm.ImageCardType.Tableau}
    return comm.ml_map_alg(fooz)


def opencv_run():
    return None



def api_endpoint():    
    #correlation comparison for ml vs opencv
        #consider which correlation to use
    #compare correlations    
    

