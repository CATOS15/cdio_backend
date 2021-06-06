import cv2
def resize_image(img):
    scale_percent = 10 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


def enlarge_image(img):
    scale_percent = 10 # percent of original size
    width = int(img.shape[1] * scale_percent )
    height = int(img.shape[0] * scale_percent)
    dim = (width, height)

    # resize image
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def print_results(images,path):
    for i,img in enumerate(images):
        cv2.imwrite(path.format(i), img)


#also can print face_values
def print_results_suits_numbers(images, path, index):
    for i,img in enumerate(images):
        cv2.imwrite(path.format(str(index)+"_"+str(i)), img)