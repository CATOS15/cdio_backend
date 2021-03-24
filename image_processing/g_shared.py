path_contours_sp1 = "image_processing/templates/card/result/sample1/image_samples/contour_res_squares_{}.png"
path_contours_sp2 = "image_processing/templates/card/result/sample2/image_samples/contour_res_squares_{}.png"
path_contours_sp3 = "image_processing/templates/card/result/sample3/image_samples/contour_res_squares_{}.png"

path_template_sp1 = "image_processing/templates/card/result/sample1/template_samples/template_{}.png"
# path_template_sp2 = "image_processing/templates/card/result/sample2/template_samples/template_{}.png"
# path_template_sp3 = "image_processing/templates/card/result/sample3/template_samples/template_{}.png"

# store results
result_image_sp1 = 'image_processing/templates/card/result/sample1/results/res_{}.png'
# result_image = 'image_processing/templates/card/result/res.png'

from enum import Enum

Suit = Enum('Suits', 'Spade Heart Diamonds Club')
Cards = Enum(
    'Cards', 'Ace Two Three Four Five Six Seven Eight Nine Ten Eleven Twelf Thirteen')
