from g_img import *
def locate_figure(template_match,threshold, width, height, color):
    thicc = 2
    loc = np.where(template_match >= threshold)
    for pt in zip(*loc[::-1]):
            cv2.rectangle(g_img_color, pt,(pt[0] + width, pt[1] + height), color, thicc)
            #send value or send suit



