import cv2
import numpy as np
from img_contour import __contour_draw

suits_numbers = "suits_numbers"
face_cards = "face_cards"


def find_by_hierachy(contours, alg1, alg2):
    face_card = 0.50
    noise = 0.0001
    cards = []

    # numbered_cards = ()
    # numbered_cards_cnt = 0, face_cards_cnt = 0

    for card in contours:
        countours, hierachy = cv2.findContours(card, alg1, alg2)
        card_size = card.shape[0] * card.shape[1]
        _face_cards = []
        _suits_numbers = []
        card_cunts = {suits_numbers: _suits_numbers, face_cards: _face_cards}


        for i, cunt in enumerate(countours):
            # for some unholy reason there is a 3rd diemension, may god save the man who inveted this course I wont
            if hierachy[0][i][3] == 0:
                # don't take face card or any template to small to recognize
                if cv2.contourArea(cunt) < face_card*card_size and cv2.contourArea(cunt) > noise*card_size:
                    _suits_numbers.append(np.array(__contour_draw(card, cunt)))
                
                elif cv2.contourArea(cunt) > face_card*card_size and cv2.contourArea(cunt) > noise*card_size:
                    _face_cards.append(np.array(__contour_draw(card, cunt)))
        
        cards.append(card_cunts)
    return cards

# relationship of a contour (-1, -1, 1, 0)
# foo = hierachy[0][0][0] #index 0
# foo1 = hierachy[0][0][1] #index 1
# foo2 = hierachy[0][0][2] #index 2
# foo3 = hierachy[0][0][3] #index 3
# foo4 = hierachy[0][1][3] #next contour relationship


# things that can go wrong
# minimum recognition is to large - we skip potential positives
# minimum recognition is to small - we get face cards

# we need to consider