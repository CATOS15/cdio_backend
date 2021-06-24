#Gruppe 15
#Christian Frost s184140
#Mikkel Lindtner s205421 
#Nikolai Stein s205469
#Oliver Christensen s176352
#Søren Andersen s182881
#Tobias Kristensen s195458

import communication_layer.ml_alg as comm

def compare_results(cv_results, ml_results):
    solitaire_alg = {}
    solitaire_alg['waste'] = comm.map_ml_alg(ml_results[0], comm.ImageCardType.Waste)
    solitaire_alg['fountains'] = comm.map_ml_alg(ml_results[1], comm.ImageCardType.Foundation)
    solitaire_alg['tableau'] = comm.map_ml_alg(ml_results[2], comm.ImageCardType.Tableau)
    return solitaire_alg