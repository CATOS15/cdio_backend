import cv2
from g_shared import path_tmpl_birck_rank_bin_inv


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

# Example
    # if tmpl_card.type == CardType.SUIT:
    #     tmpl_bin_inv(tmpl_card.img, path_tmpl_birck_suit_bin_inv, tmpl_card.value.name)

    # if tmpl_card.type == CardType.RANK:
    #     tmpl_bin_inv(tmpl_card.img, path_tmpl_birck_rank_bin_inv, tmpl_card.value.name)