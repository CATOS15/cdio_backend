import cv2
import image_processing.g_img as g_img

def store_images(images, path):
    for i, img in enumerate(images):
        cv2.imwrite(path.format(i), img)

# MORMORS MØRKERUM BITCH'ÈS
def wash_img(img, cunts_1_sample):
    wash_split_img = []
    for img_sample1 in cunts_1_sample:
        wash_split_img.append(img_sample1)

    # use OSTU to clear up noice from cards
    img_1_clear = __contrast_flip_images(
        wash_split_img, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    store_images(img_1_clear, g_img.path_contours_sp2)

    return img_1_clear


def templ_threshold(templInfo, lower, upper):
    cv2.threshold(templInfo.templ_image, lower, upper, 0)


def __contrast_flip_images(img_cunts, alg1):
    imgs = []
    for i, cunt in enumerate(img_cunts):
        blur = cv2.GaussianBlur(cunt, (5, 5), 0)
        ret3, th3 = cv2.threshold(
            blur, 0, 255, alg1)
        imgs.append(th3)
    return imgs


def adaptive_wash(image, alg1):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gaus_kernel_size = (5,5)
    blur = cv2.GaussianBlur(gray,gaus_kernel_size,0)
    C = 3 #dependant on on resolution used together with blocksize
    white = 255
    block_size = 13 #dependant on resolution
    
    #adapt to lightning
    thresh = cv2.adaptiveThreshold(blur, white, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, alg1, block_size, C)

    return thresh

def otsu_wash(image, alg1):
    black = 0
    white = 255
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (1,1), 0)
    _, th3 = cv2.threshold(blur, black, white, alg1+cv2.THRESH_OTSU)
    return th3 