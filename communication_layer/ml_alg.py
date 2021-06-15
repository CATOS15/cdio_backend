import ml_solitaire.yolov5v2.result
import ml_solitaire.transform720
from enum import Enum
import image_processing.img_contour
import image_processing.img_wash
import cv2
import image_processing.g_shared
# import image_processing.templates.test.full_deck

path_img = "communication_layer/img{}.png"


class ImageCardType(Enum):
    Waste = 1
    Foundation = 2
    Tableau = 3
    Column = 4

# from ml to alg


# examples(dict_images: [path/image object : ImageCardType])
opencvbilledobjekt = cv2.imread("image.jpg")

# dict_images = {
#     {"img_obj": opencvbilledobjekt, "ImageCardType": 1},
#     {"img_obj2": opencvbilledobjekt, "ImageCardType": 1},
#     {"img_obj3": opencvbilledobjekt, "ImageCardType": 1},
# }

# dict_images_withpath = {
#         {"path" : "/her", "ImageCardType" : 1},
#         {"path" : "/her", "ImageCardType" : 1},
#     }

# examples(dict_images: [path : ImageCardType])


def ml_map_alg(dict_images):
    data_solitaire = {
        'stacks': [
        ],
        'fountains': [
        ],
        'cardpile': [
        ],
    }



    #print(dict_images)

    #run yolo recognition thingy here
    counter = 0
    for img_type, img in dict_images.items():
        if img_type == ImageCardType.Tableau:
            for im in img:
                yellowBG = ml_solitaire.transform720.transform_720(im)
                cv2.imwrite(path_img.format(counter), yellowBG)
                counter += 1
                img = yellowBG
        else:
            yellowBG = ml_solitaire.transform720.transform_720(img)
            cv2.imwrite(path_img.format(counter), yellowBG)
            counter += 1
            img = yellowBG


    for img_type, img in dict_images.items():
        #print(img)
        result_set = ml_solitaire.yolov5v2.result.getCardsFromImage(img)

        if img_type == ImageCardType.Tableau:
            for col in img:    
                col_set = ml_solitaire.yolov5v2.result.getCardsFromImage(col)
                ml_solitaire.yolov5v2.result.addStackToTableau(col_set, data_solitaire)
        elif img_type == ImageCardType.Foundation:
            ml_solitaire.yolov5v2.result.addToFountain(result_set, data_solitaire)
        elif img_type == ImageCardType.Waste:
            ml_solitaire.yolov5v2.result.addToWaste(result_set, data_solitaire)

    return data_solitaire


def opencv_ml_tableau_columns_color(img_tableau, has_background=False):
    thresh = image_processing.img_wash.otsu_wash(img_tableau, cv2.THRESH_BINARY)
    columns_color = image_processing.img_contour.contours_cut_columns(thresh, img_tableau, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i, column in enumerate(columns_color):
        cv2.imwrite(image_processing.g_shared.path_contours_sp1.format(i), column)
    return columns_color



