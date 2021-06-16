from image_processing.img_wash import templ_threshold
import cv2
import image_processing.debugging as debugging

#always scale down - doesn't work
def ratio_img_resolution(img_from, img_template):
    # has_swapped = False
    # img_res = img_from.shape[0] * img_from.shape[1]
    # tmpl_area = img_template.shape[0] * img_template.shape[1]

    # # same resolution
    if img_from.shape[0] == img_template.shape[0] and img_from.shape[1] == img_template.shape[1]:
        return (img_from, img_template)

    # resized_img = img_from
    # resized_template = img_template
    # height = 0
    # width = 1

    return (img_from, cv2.resize(img_template, (img_from.shape[0], img_from.shape[1])))

    # height scale template/image down
    # if img_from.shape[height] < img_template.shape[height]:
    #     scale_height = img_from.shape[height] / img_template.shape[height]
    #     new_height = int(img_template.shape[height] * scale_height)
    #     resized_template = cv2.resize(img_template, (img_template.shape[width], new_height))
    # else:
    #     scale_height = img_template.shape[height] / img_from.shape[height]
    #     new_height = int(img_from.shape[height]*scale_height)
    #     resized_img = cv2.resize(img_from, (img_from.shape[width], new_height))

    # # width
    # if img_from.shape[width] < img_template.shape[width]:
    #     scale_width = img_from.shape[width] / img_template.shape[width]
    #     new_width = int(scale_width * img_template.shape[width])
    #     resized_template = cv2.resize(img_template, (new_width, img_template.shape[height]))
    # else:    
    #     scale_width = img_template.shape[width] / img_from.shape[width]
    #     new_width = int(scale_width * img_from.shape[width])
    #     resized_img = cv2.resize(img_from, (new_width, img_from.shape[height]))

    # return (resized_img, resized_template)
    # always downsize instead of upsize
    # if img_res - template_res < 0:
    #     tmp = img_from
    #     img_from = img_template
    #     img_template = tmp
    #     has_swapped = True
    # debugging.count_err += 1

    # # scale from to match ideal
    # scale_height = img_template.shape[0] / img_from.shape[0]
    # scale_width = img_template.shape[1] / img_from.shape[1]
    # new_height = int(img_from.shape[0] * scale_height)
    # new_width = int(img_from.shape[1] * scale_width)

    # index 0 is always img_from, index 1 is always img_ideal
    # if has_swapped == False:
    #     return (img_from, cv2.resize(img_template, (new_width, new_height)))
    # else:
    #     return (cv2.resize(img_from,(new_width, new_height)), img_template)


def ratio_img_resolution2(img_from, img_template):
    height = 0
    width = 1

    img_from_new_height, img_from_new_width = img_from.shape
    img_template_new_height, img_template_new_width = img_template.shape

    if img_from.shape[height] == img_template.shape[height] and img_from.shape[width] == img_template.shape[width]:
        return img_from, img_template

    # Correct width
    if img_from.shape[width] > img_template.shape[width]:
        img_from_new_width = img_template.shape[width]
    elif img_from.shape[width] < img_template.shape[height]:
        img_template_new_width = img_from.shape[width]

        # Correct height
    if img_from.shape[height] > img_template.shape[height]:
        img_from_new_height =  img_template.shape[height]
    elif img_from.shape[height] < img_template.shape[height]:
        img_template_new_height = img_from.shape[height]

    return (cv2.resize(img_from, (img_from_new_height, img_from_new_width)), cv2.resize(img_template, (img_template_new_height, img_template_new_width)))


def ratio_template_resolution(img_templates, avg_columns_width, ideal_width, ideal_height):
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
