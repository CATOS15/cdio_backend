import cv2
import image_processing.g_shared as g_shared
# from g_shared import path_tmpl_birck_rank_bin_inv
# from g_shared import path_contours_sp3

count_err = 0

def resize_image(img):
    scale_percent = 10  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def enlarge_image(img):
    scale_percent = 10  # percent of original size
    width = int(img.shape[1] * scale_percent)
    height = int(img.shape[0] * scale_percent)
    dim = (width, height)

    # resize image
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def print_results(images, path):
    for i, img in enumerate(images):
        cv2.imwrite(path.format(i), img)


# also can print face_values
def print_results_suits_numbers(images, path, index):
    for i, img in enumerate(images):
        cv2.imwrite(path.format(str(index)+"_"+str(i)), img)


# use this for storing images temporary
def tmpl_bin_inv(color_img, path, card_name):
    grey_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    flipped = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(flipped, (5, 5), 0)
    _, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imwrite(path.format(card_name), th)


def print_waste_cuts(flow_waste_cuts):
    cnt = 0
    for card in flow_waste_cuts:
        for cuts in card["suits_numbers"]:
            cv2.imwrite(g_shared.path_contours_sp3.format(cnt), cuts)
            cnt += 1


def print_ml_results(fraction_name, results):
    print("-----" + fraction_name + "------")
    for column in results:
        print('[', end = '')
        for card in column:
            print(card)
        print(']')

    #Examples
    # print("-----waste:-----")
    # for column in waste_results:
    #     print('[', end = '')
    #     for card in column:
    #         print(card)
    #     print(']')

    # print("-----foundation:-----")
    # for column in foundation_results:
    #     print('[', end = '')
    #     for card in column:
    #         print(card)
    #     print(']')

    # print("-----tableau:-----")
    # for column in tableau_results:
    #     print('[', end = '')
    #     for card in column:
    #         print(card)
    #     print(']')

# Example
    # if tmpl_card.type == CardType.SUIT:
    #     tmpl_bin_inv(tmpl_card.img, path_tmpl_birck_suit_bin_inv, tmpl_card.value.name)

    # if tmpl_card.type == CardType.RANK:
    #     tmpl_bin_inv(tmpl_card.img, path_tmpl_birck_rank_bin_inv, tmpl_card.value.name)

