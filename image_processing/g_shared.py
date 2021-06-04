#Remember to open the project in cdio_backend for the relative path to work
path_contours_sp1 = "image_processing/templates/card/result/sample1/image_samples/contour_res_squares_{}.png"
path_contours_sp2 = "image_processing/templates/card/result/sample2/image_samples/contour_res_squares_{}.png"
path_contours_sp3 = "image_processing/templates/card/result/sample3/image_samples/contour_res_squares_{}.png"
path_contours_sp4 = "image_processing/templates/card/result/sample4/image_samples/contour_res_squares_{}.png"

path_template_sp1 = "image_processing/templates/card/result/sample1/template_samples/template_{}.png"
# path_template_sp2 = "image_processing/templates/card/result/sample2/template_samples/template_{}.png"
# path_template_sp3 = "image_processing/templates/card/result/sample3/template_samples/template_{}.png"

# store results
result_image_sp1 = 'image_processing/templates/card/result/sample1/results/res_{}{}.png'
result_image_sp2 = 'image_processing/templates/card/result/sample2/results/res_{}{}.png'


#Templates for making a template (lmao)
path_template_number = 'image_processing/templates/number/3_red_diamond_number_template.png'
path_template_suit_diamonds = 'image_processing/templates/suits/3_diamonds_suit_template.png'
path_template_suit_hearts = 'image_processing/templates/suits/3_hearts_suit_template.png'



from enum import Enum

Suit = Enum('Suits', 'Spade Heart Diamonds Club')
Cards = Enum(
    'Cards', 'Ace Two Three Four Five Six Seven Eight Nine Ten Eleven Twelf Thirteen')


#TRASH
path_card_waste = 'image_processing/templates/test/waste.png'