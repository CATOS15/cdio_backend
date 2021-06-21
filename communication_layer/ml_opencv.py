import communication_layer.ml_alg as comm

def compare_results(cv_results, ml_results):
    solitaire_alg = {}
    solitaire_alg['waste'] = comm.map_opencv_alg(cv_results[0], comm.ImageCardType.Waste)
    solitaire_alg['fountains'] = comm.map_opencv_alg(ml_results[1], comm.ImageCardType.Foundation)
    solitaire_alg['tableau'] = comm.map_opencv_alg(ml_results[2], comm.ImageCardType.Tableau)
    return solitaire_alg