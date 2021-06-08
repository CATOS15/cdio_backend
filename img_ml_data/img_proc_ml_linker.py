from image_processing.img_recognition import *


def find_columns_color(img):
    # find card outlines
    flow_waste_washed = flow_waste.execute_wash(img, cv2.THRESH_BINARY)

    # cut these outlines
    flow_waste_countours = flow_waste.execute_contour(
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_waste_washed, img_color=test)

    return flow_waste_countours


def find_columns_bin(img):
    # find card outlines
    flow_waste_washed = flow_waste.execute_wash(img, cv2.THRESH_BINARY)

    # cut these outlines
    flow_waste_countours = flow_waste.execute_contour(
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=flow_waste_washed, img_color=test)

    # cut suit and number
    washed_images = []
    for i, cunt in enumerate(flow_waste_countours):
        washed_images.append(flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

    return washed_images