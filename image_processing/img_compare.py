import cv2
import numpy as np


# suits must be templateInfo
def compare(img_color, washed_images, suits, numbers):
    suit_matches = []
    number_matches = []
    for washed_img in washed_images:
        for suit in suits:
            suit_matches.append(locate_figure(img_color, washed_img, suit))
            # suit_matches.append(suit.compare_template(washed_img))
        for number in numbers:
            number_matches.append(locate_figure(img_color, washed_img, number))
            # number_matches.append(number.compare_template(washed_img))
    return suit_matches, number_matches


def locate_figure(img_color, washed_image, templ):
    matches = templ.compare_template(washed_image)
    loc = np.where(matches >= templ.threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(
            washed_image, pt, (pt[0] + templ.width, pt[1] + templ.height), templ.drawSquare.color, templ.drawSquare.thicc)
    return washed_image

    # return img_color


def write_to(dst, res_suits, res_numbers):
    for i,res in enumerate(res_suits):
        cv2.imwrite(dst.format("suit_",i), res)

    for i,res in enumerate(res_numbers):
        cv2.imwrite(dst.format("numbers_",i), res)