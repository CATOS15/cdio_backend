#I HAVE A SHITTY LINTER, DON'T JUDGE
from g_img import *
from img_map import *
from img_compare import *

# path_card_high_res = './image_processing/templates/test/3_diamonds_hearts_high_res.png'
path_card_high_res = './image_processing/templates/test/many_cards_bad_lighting_1.png'
high_res_color = cv2.imread(path_card_high_res)

img_input = set_resolution(high_res_color, g_img_color)

#images is sinlge image, made into multiple small high-conctrast images
washed_images = wash_img(img_input)
results = compare(img_input, washed_images, g_suits, g_numbers)

for i,res in enumerate(results):
    cv2.imwrite(result_image_sp1.format(i), res)



# img3 = locate_figure(img_grey, img_grey, g_templ_objs['diamond'])

# heart, diamonds, number = match_template_suit(img_grey, g_match_alg)
# img1 = locate_figure(img_input, img_grey, g_templ_objs['heart'])
# img2 = locate_figure(img1, img_grey, g_templ_objs['diamond'])
# img3 = locate_figure(img2, img_grey, g_templ_objs['number'][Cards.Three])

# cv2.imwrite(result_image, img3)


#TODO
#Get a match w. templateMethod at 80%
    #1 suit
        #consider different algorithms
        #consider changing templateMethod to check for grey

            #multiple suits
    #1 number
        #multiple numbers
#Write square into original image


#stuff
# Feature Detection 
    #Feature Description