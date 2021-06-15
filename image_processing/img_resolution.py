import cv2

def ratio_img_resolution(img_from, img_ideal):
    has_swapped = False
    img_from_res = img_from.shape[0] * img_from.shape[1]
    img_ideal_res = img_ideal.shape[0] * img_ideal.shape[1]

    # same resolution
    if img_from_res - img_ideal_res == 0:
        return img_from
    
    #always downsize instead of upsize
    if img_from_res - img_ideal_res < 0:
        tmp = img_from
        img_from = img_ideal
        img_ideal = tmp
        has_swapped = True
    
    # scale from to match ideal
    scale_height = img_ideal.shape[0] / img_from.shape[0]
    scale_width = img_ideal.shape[1] / img_from.shape[1]
    new_height = int(img_from.shape[0] * scale_height)
    new_width = int(img_from.shape[1] * scale_width)

    #index 0 is always img_from, index 1 is always img_ideal
    if has_swapped == False:
        return (img_from, cv2.resize(img_ideal, (new_height, new_width)))
    else:
        return (cv2.resize(img_from,(new_width, new_height)), img_ideal)
    

def ratio_template_resolution(img_templates,avg_columns_width,ideal_width,ideal_height):
    new_height = int(ideal_height * avg_columns_width)
    new_width = int(ideal_width * avg_columns_width)

    for template in img_templates:
        resized_template = cv2.resize(template.templ_image, (new_width, new_height))
        template.templ_image = resized_template
        template.width = resized_template.shape[1]
        template.height = resized_template.shape[0]
    return img_templates


def avg_columns_width(washed_images):
    total_width = 0

    for img in washed_images:
        total_width += img.shape[1]

    return int(total_width/len(washed_images))


def bin_invert_templates(g_templates):
    for tmpl in g_templates:
        grey_img = cv2.cvtColor(tmpl.img, cv2.COLOR_BGR2GRAY)
        flipped = cv2.bitwise_not(grey_img)
        blur = cv2.GaussianBlur(flipped, (5, 5), 0)
        _, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        tmpl.img = th
    return g_templates  