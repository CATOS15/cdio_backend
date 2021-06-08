import os
import cv2
import sys
import image_processing.debugging as debugging
import image_processing.flows as flows
import image_processing.g_shared as g_shared
import pathlib

# path_img_ml_col = os.getcwd() + '\\\\img_ml_data\\\\columns'
path_waste1 = "../" + g_shared.path_card_waste #refacotr this

img_color = cv2.imread(path_waste1, cv2.IMREAD_COLOR)

def find_columns_color(img):
    # find card outlines
    flow_waste_washed = flows.flow_waste.execute_wash(img, cv2.THRESH_BINARY)

    # cut these outlines
    flow_waste_countours = flows.flow_waste.execute_contour(
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_waste_washed, img_color=img)

    f = str(pathlib.Path(os.getcwd(), "img_ml_data/columns/color/color_img_{}.png"))
    debugging.print_results(flow_waste_countours, f)
    return flow_waste_countours


def find_columns_bin(img):
    # find card outlines
    flow_waste_washed = flows.flow_waste.execute_wash(img, cv2.THRESH_BINARY)

    # cut these outlines
    flow_waste_countours = flows.flow_waste.execute_contour(
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_waste_washed, img_color=img)

    # cut suit and number
    washed_images = []
    for i, cunt in enumerate(flow_waste_countours):
        washed_images.append(flows.flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

    # print_results(flow_waste_countours, path_img_ml_col+'/bin')
    # return washed_images

a = find_columns_color(g_shared.test)
# print(a)