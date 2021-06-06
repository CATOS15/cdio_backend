import cv2
import numpy as np
from img_cut_suit_rank import suits_numbers
from img_resolution import ratio_img_resolution
from g_img import * 
from g_img import CardType


template_match_alg = cv2.TM_CCOEFF_NORMED


def compare_templates(cards, template):
    # template_match_results = [] #results for one template / one column / one card

    suit = None
    rank = None
    suit_threshold = 0
    rank_threshold = 0


    for card in cards:
        for _, cunt in enumerate(card[suits_numbers]):
            rzimage, rztemplate = ratio_img_resolution(cunt, template.img) #match each contour to the size of a template
            match = cv2.matchTemplate(rzimage, rztemplate, template_match_alg)
            # loc = np.where(match >= template.threshold)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
            
            #assumes max val is a sum of all points of the euclidian gitter
            f = template.type
            if f == CardType.SUIT:
                if suit == None or max_val > suit_threshold:
                    suit = template.value
                    suit_threshold = max_val
                # if suit == None or min_val < suit_threshold:
                #     suit = template.value
                #     suit_threshold = min_val

            if template.type == CardType.RANK:
                if rank == None or max_val > rank_threshold:
                    rank = template.value
                    rank_threshold = max_val
            #     if rank == None or min_val < rank_threshold:
            #         rank = template.value
            #         rank_threshold = min_val

    return (suit, rank, suit_threshold, rank_threshold)


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