import ml_solitaire.yolov5v2.result
from enum import Enum


class ImageCardType(Enum):
    Waste = 1
    Fountain = 2
    Tableau = 3

# from ml to alg
def ml_map_alg(path_to_img, ict):
    data_solitaire = {
        'stacks': [
        ],
        'fountains': [
        ],
        'cardpile': [
        ],
    }
    result_set = ml_solitaire.yolov5v2.result.getCardsFromImage(path_to_img)
    if ict == ImageCardType.Tableau:
        ml_solitaire.yolov5v2.result.addStackToTableau(result_set, data_solitaire)
    elif ict == ImageCardType.Fountain:
        ml_solitaire.yolov5v2.result.addToFountain(result_set, data_solitaire)
    elif ict == ImageCardType.Waste:
        ml_solitaire.yolov5v2.result.addToWaste(result_set, data_solitaire)

    return data_solitaire

# from opencv to ml


# def opencv_ml():
#     return None


# ml_map_alg("ml_solitaire/yolov5v2/tableau.jpg", ImageCardType.Tableau)