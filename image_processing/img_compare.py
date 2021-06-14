import enum
import cv2
import numpy as np
import image_processing.img_cut_suit_rank as cut_suit_rank
import image_processing.g_img as g_img
import image_processing.img_resolution as resolution
import image_processing.objects as objects

# Ways to compute euclidian kernel w. Original Image
# cv2.TM_CCOEFF
# cv2.TM_CCOEFF_NORMED  # this works best so far
# cv2.TM_SQDIFF
# cv2.TM_SQDIFF_NORMED
# cv2.TM_CCORR
# cv2.TM_CCORR_NORMED

template = cv2.TM_CCOEFF_NORMED


def compare_ranksuit(card, g_templates):
    finished_card = objects.Card(None, None, None, None)

    for tmpl in g_templates:
        for _, cunt in enumerate(card[cut_suit_rank.suits_numbers]):
            rzimage, rztemplate = resolution.ratio_img_resolution(cunt, tmpl.img)
            match = cv2.matchTemplate(
                rzimage, rztemplate, template)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)

            if template is not(cv2.TM_SQDIFF or cv2.TM_SQDIFF_NORMED):
                _compare_suit_rank_max(finished_card, tmpl, max_val)
            else:
                _compare_suit_rank_min(finished_card, tmpl, min_val)

    return finished_card

# use for coeff/coeff_normed, corr/corr_normed


def _compare_suit_rank_max(card, template, max_val):
    if template.type == g_img.CardType.SUIT:
        if (card.suit == None or max_val > card.suit_threshold) and max_val > g_img.g_threshold_suit:
            card.suit = template.value
            card.suit_threshold = max_val

    if template.type == g_img.CardType.RANK:
        if (card.rank == None or max_val > card.rank_threshold) and max_val > g_img.g_threshold_rank:
            card.rank = template.value
            card.rank_threshold = max_val


# use for sqdiff/sqdiff_normed
def _compare_suit_rank_min(card, template, min_val):
    if template.type == g_img.CardType.SUIT:
        if (card.suit == None or min_val < card.suit_threshold) and min_val < g_img.g_threshold_suit:
            card.suit = template.value
            card.suit_threshold = min_val

    if template.type == g_img.CardType.RANK:
        if (card.rank == None and min_val < card.rank_threshold) and min_val < g_img.g_threshold_rank:
            card.rank = template.value
            card.rank_threshold = min_val


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
    for i, res in enumerate(res_suits):
        cv2.imwrite(dst.format("suit_", i), res)

    for i, res in enumerate(res_numbers):
        cv2.imwrite(dst.format("numbers_", i), res)
