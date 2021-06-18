import cv2
import ml_solitaire.transform720
import image_processing.img_wash
import image_processing.g_shared
import image_processing.img_contour
import ml_solitaire.yolov5v2.result

from enum import Enum

path_img = "communication_layer/img{}.png"

class ImageCardType(Enum):
    Waste = 1
    Foundation = 2
    Tableau = 3
    Column = 4

number = 'number'
suit = 'suit'


def map_opencv_alg(solution, type):
    converted_to_alg = []
    if type == ImageCardType.Waste:
        for card in solution:
            json_card = _convert_cardobj_alg(card)
            if json_card != None:
                converted_to_alg.append(json_card)

    if type == ImageCardType.Foundation:
        for x in range(1, 5):
            found_card = False
            for card in solution:
                if card.suit == None:
                    continue
                if card.suit.value == x:
                    json_card = _convert_cardobj_alg(card)
                    if json_card == None:
                        json_card = _foundation_set_none(x)
                    converted_to_alg.append(json_card)
                    found_card = True
                    break

            if found_card == False:
                alg_card = _foundation_set_none(x)
                converted_to_alg.append(alg_card)

    if type == ImageCardType.Tableau:        
        for col in solution:
            column_arr = []
            for card in col:
                json_card = _convert_cardobj_alg(card)
                column_arr.append(json_card)
            converted_to_alg.append(column_arr)
    return converted_to_alg


def _foundation_set_none(suit_val):
    foo = {}
    foo[number] = 0
    foo[suit] = suit_val
    return foo


def _convert_cardobj_alg(card):
    if card.rank == None or card.suit == None:
        return None
    return {number: card.rank.value, suit: card.suit.value}


def ml_map_alg(dict_images):
    data_solitaire = {
        'stacks': [
        ],
        'fountains': [
        ],
        'cardpile': [
        ],
    }

    # run yolo recognition thingy here
    counter = 0
    for img_type, img in dict_images.items():
        if img_type == ImageCardType.Tableau:
            changed_img = []
            for im in img:
                yellowBG = ml_solitaire.transform720.transform_720(im)
                changed_img.append(yellowBG)
            dict_images[img_type] = changed_img
        else:
            yellowBG = ml_solitaire.transform720.transform_720(img)
            dict_images[img_type] = yellowBG

    for img_type, img in dict_images.items():
        counter += 1
        if img_type is not ImageCardType.Tableau:
            result_set = ml_solitaire.yolov5v2.result.getCardsFromImage(img)

        if img_type == ImageCardType.Tableau:
            for col in img:
                counter += 1
                col_set = ml_solitaire.yolov5v2.result.getCardsFromImage(col)
                ml_solitaire.yolov5v2.result.addStackToTableau(col_set, data_solitaire)
        elif img_type == ImageCardType.Foundation:
            ml_solitaire.yolov5v2.result.addToFountain(result_set, data_solitaire)
        elif img_type == ImageCardType.Waste:
            ml_solitaire.yolov5v2.result.addToWaste(result_set, data_solitaire)

    return data_solitaire


def opencv_ml_tableau_columns_color(img_tableau, has_background=False):
    thresh = image_processing.img_wash.otsu_wash(img_tableau, cv2.THRESH_BINARY)
    columns_color = image_processing.img_contour.contours_cut_columns(cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, thresh, img_tableau)
    for i, column in enumerate(columns_color):
        cv2.imwrite(image_processing.g_shared.path_contours_sp1.format(i), column)
    return columns_color