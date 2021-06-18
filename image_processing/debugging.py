import cv2
import math
import image_processing.g_shared as g_shared

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
        print('[', end='')
        for card in column:
            print(card)
        print(']')


def print_image_info(img):
    print(img.shape)
    # get dimensions of image
    dimensions = img.shape
    
    # height, width, number of channels in image
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    print('Image Dimension    : ',dimensions)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)



def cut_7_images(img):
    #dimensions for image
    height = img.shape[0]
    width = img.shape[1]
    heightratio = 7/24 #1/3, 7/24 or 1/4
    #cropped image *zones
    top_height = math.floor(height*1/3)

    #cropped images
    column1 = img[top_height:height, 0:math.floor(width*1/7)]
    column2 = img[top_height:height, math.floor(width*1/7):math.floor(width*2/7)]
    column3 = img[top_height:height, math.floor(width*2/7):math.floor(width*3/7)]
    column4 = img[top_height:height, math.floor(width*3/7):math.floor(width*4/7)]
    column5 = img[top_height:height, math.floor(width*4/7):math.floor(width*5/7)]
    column6 = img[top_height:height, math.floor(width*5/7):math.floor(width*6/7)]
    column7 = img[top_height:height, math.floor(width*6/7):width]

    #save images
    cv2.imwrite('ml_solitaire\image_column1.jpg', column1)
    cv2.imwrite('ml_solitaire\image_column2.jpg', column2)
    cv2.imwrite('ml_solitaire\image_column3.jpg', column3)
    cv2.imwrite('ml_solitaire\image_column4.jpg', column4)
    cv2.imwrite('ml_solitaire\image_column5.jpg', column5)
    cv2.imwrite('ml_solitaire\image_column6.jpg', column6)
    cv2.imwrite('ml_solitaire\image_column7.jpg', column7)

def show_cut_images(img):
    drawpile_path = 'ml_solitaire\image_drawpile.jpg'
    fountain_path = 'ml_solitaire\image_fountain.jpg'
    piles_path = 'ml_solitaire\image_piles.jpg'

    image_drawpile = cv2.imread(drawpile_path)
    image_fountain = cv2.imread(fountain_path)
    image_piles = cv2.imread(piles_path)

    cv2.imshow("cropped", image_drawpile)
    cv2.waitKey(0)

    cv2.imshow("cropped", image_fountain)
    cv2.waitKey(0)

    cv2.imshow("cropped", image_piles)
    cv2.waitKey(0)


def save_blackwhite_inverted_g_templates(path):
    for i,tmpl in enumerate(g_shared.g_templates):
        tmp = tmpl
        grey_img = cv2.cvtColor(tmp.img, cv2.COLOR_BGR2GRAY)
        flipped = cv2.bitwise_not(grey_img)
        cv2.imwrite(path.format(i), flipped)