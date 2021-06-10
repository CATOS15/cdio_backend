import ml_solitaire.yolov5v2.result
from enum import Enum


class ImageCardType(Enum):
    Waste = 1
    Fountain = 2
    Tableau = 3

# from ml to alg

#examples(dict_images: [path : ImageCardType])
def ml_map_alg(dict_images):
    data_solitaire = {
        'stacks': [
        ],
        'fountains': [
        ],
        'cardpile': [
        ],
    }

    for path_to_img, img_type in dict_images:
        result_set = ml_solitaire.yolov5v2.result.getCardsFromImage(path_to_img)
        if img_type == ImageCardType.Tableau:
            ml_solitaire.yolov5v2.result.addStackToTableau(result_set, data_solitaire)
        elif img_type == ImageCardType.Fountain:
            ml_solitaire.yolov5v2.result.addToFountain(result_set, data_solitaire)
        elif img_type == ImageCardType.Waste:
            ml_solitaire.yolov5v2.result.addToWaste(result_set, data_solitaire)

    return data_solitaire

# from opencv to ml


def opencv_ml_tableau():
    return None

