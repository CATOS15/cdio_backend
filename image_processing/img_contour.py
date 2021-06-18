import cv2
import numpy as np


def define_threshold(img, lower, upper):
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # use threshold to identify patterns
    _, thresh_sample1 = cv2.threshold(img_grey, lower, upper, 0)
    return thresh_sample1


def contours_cut_columns(alg1, alg2, img_thresh, img_color):
    contours, _ = cv2.findContours(
        img_thresh, alg1, alg2)
    #sort left-to-right
    boundingBoxes = [cv2.boundingRect(c) for c in contours]
    (cunts, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b:b[1][0], reverse=False))
    
    img_cunts = []
    cuntour_area_req = 42500
    # contours
    for cunt in cunts:
        if cv2.contourArea(cunt) > cuntour_area_req:
            img_cunts.append(np.array(__contour_draw(img_color, cunt)))
    #sort left to right
    return img_cunts


def contour_approximation(alg1, alg2, img_thresh, img_color=None):
    cunt_flattened = []
    
    # Find cunts
    contours, _ = cv2.findContours(img_thresh, alg1, alg2)

    # Find approximations
    cuntour_area_req = 42500
    for cunt in contours:
        if cv2.contourArea(cunt) > cuntour_area_req:
            # Find approximation
            epsilon = 0.01*cv2.arcLength(cunt, True)
            approx = cv2.approxPolyDP(cunt, epsilon, True)
            _, _, w, h = cv2.boundingRect(approx)
            pts = np.float32(approx)
            # flattening
            if img_color.any() != None:
                cunt_flattened.append(flat_image(img_color, pts, w, h))
            else:
                cunt_flattened.append(flat_image(img_thresh, pts, w, h))
                
    return cunt_flattened


# NB! Code taken from: www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
# makes a small x*x image for a single contour
def flat_image(image, pts, w, h):
    temp_rect = np.zeros((4, 2), dtype="float32")
    s = np.sum(pts, axis=2)

    #top left, buttom right, top right, bottom left of the image
    tl = pts[np.argmin(s)]
    br = pts[np.argmax(s)]

    diff = np.diff(pts, axis=-1)
    tr = pts[np.argmin(diff)]
    bl = pts[np.argmax(diff)]

    if w <= 0.8*h:  # If card is vertically oriented
        temp_rect[0] = tl
        temp_rect[1] = tr
        temp_rect[2] = br
        temp_rect[3] = bl

    if w >= 1.2*h:  # If card is horizontally oriented
        temp_rect[0] = bl
        temp_rect[1] = tl
        temp_rect[2] = tr
        temp_rect[3] = br

    # If the card is 'diamond' oriented, a different algorithm
    # has to be used to identify which point is top left, top right
    # bottom left, and bottom right.

    if w > 0.8*h and w < 1.2*h:  # If card is diamond oriented
        # If furthest left point is higher than furthest right point,
        # card is tilted to the left.
        if pts[1][0][1] <= pts[3][0][1]:
            # If card is titled to the left, approxPolyDP returns points
            # in this order: top right, top left, bottom left, bottom right
            temp_rect[0] = pts[1][0]  # Top left
            temp_rect[1] = pts[0][0]  # Top right
            temp_rect[2] = pts[3][0]  # Bottom right
            temp_rect[3] = pts[2][0]  # Bottom left

        # If furthest left point is lower than furthest right point,
        # card is tilted to the right
        if pts[1][0][1] > pts[3][0][1]:
            # If card is titled to the right, approxPolyDP returns points
            # in this order: top left, bottom left, bottom right, top right
            temp_rect[0] = pts[0][0]  # Top left
            temp_rect[1] = pts[3][0]  # Top right
            temp_rect[2] = pts[2][0]  # Bottom right
            temp_rect[3] = pts[1][0]  # Bottom left
    
    # maxWidth = 200
    # maxHeight = 300
    width_buttom = (br[0][0] - bl[0][0]) ** 2 + ((br[0][1] - bl[0][1]) ** 2)
    width_top = (tr[0][0] - tl[0][0]) ** 2 + ((tr[0][1] - tl[0][1]) ** 2)
    # widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    # widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    widthA = np.sqrt(width_buttom)
    widthB = np.sqrt(width_top)
    maxWidth = max(int(widthA), int(widthB))

    height_buttom = (tr[0][0] - br[0][0]) ** 2 + ((tr[0][1] - br[0][1]) ** 2)
    height_top = (tl[0][0] - bl[0][0]) ** 2 + ((tl[0][1] - bl[0][1]) ** 2)
    heightA = np.sqrt(height_buttom)
    heightB = np.sqrt(height_top)
    maxHeight = max(int(heightA), int(heightB))

    #frame for perspective in transofrmation
    dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

    # Create destination array, calculate perspective transform matrix,
    # and warp card image
    M = cv2.getPerspectiveTransform(temp_rect,dst)
    warp = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warp


def __contour_draw(adaptive_th, cunt):
    rect = cv2.minAreaRect(cunt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(adaptive_th, cunt, 0, (0, 0, 255), 2)
    x, y, w, h = cv2.boundingRect(cunt)
    return adaptive_th[y:y + h, x:x + w]
