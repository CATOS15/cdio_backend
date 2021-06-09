import os
import cv2
import sys
import image_processing.debugging as debugging
import image_processing.flows as flows
import image_processing.g_shared as g_shared
import pathlib

path_waste1 = "../" + g_shared.path_card_waste #refacotr this

img_output = str(pathlib.Path(os.getcwd(), "img_ml_data/columns/color/color_img_{}.png"))
 
def find_columns_color(img):
    # find card outlines
    flow_waste_washed = flows.flow_waste.execute_wash(img, cv2.THRESH_BINARY)

    # cut these outlines
    flow_waste_countours = flows.flow_waste.execute_contour(
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_waste_washed, img_color=img)

    debugging.print_results(flow_waste_countours, img_output)
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


#see set python path: https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c
cv2.imread("3.jpg", 0)
a = find_columns_color(g_shared.test)
