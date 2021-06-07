from enum import Enum
path_templates = 'image_processing/templates'
path_tmpl_birck_rank = path_templates + '/number/birck_rank/'
path_tmpl_birck_suit = path_templates + '/suits/birck_suit/'
path_tmpl_birck_rank_bin_inv = path_tmpl_birck_rank + 'bin_inverted/{}.png'
path_tmpl_birck_suit_bin_inv = path_tmpl_birck_suit + 'bin_inverted/{}.png'

# Remember to open the project in cdio_backend for the relative path to work
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


#Template suit filepath
path_template_suit_club = path_tmpl_birck_suit + 'suit_club.png'
path_template_suit_diamond = path_tmpl_birck_suit + 'suit_diamond.png'
path_template_suit_heart = path_tmpl_birck_suit + 'suit_heart.png'
path_template_suit_spade = path_tmpl_birck_suit + 'suit_spade.png'

#Template rank filepath
path_template_rank_2 = path_tmpl_birck_rank + 'rank_2.png'
path_template_rank_3 = path_tmpl_birck_rank + 'rank_3.png'
path_template_rank_4 = path_tmpl_birck_rank + 'rank_4.png'
path_template_rank_5 = path_tmpl_birck_rank + 'rank_5.png'
path_template_rank_6 = path_tmpl_birck_rank + 'rank_6.png'
path_template_rank_7 = path_tmpl_birck_rank + 'rank_7.png'
path_template_rank_8 = path_tmpl_birck_rank + 'rank_8.png'
path_template_rank_9 = path_tmpl_birck_rank + 'rank_9.png'
path_template_rank_10 = path_tmpl_birck_rank + 'rank_10.png'
path_template_rank_jack = path_tmpl_birck_rank + 'rank_jack.png'
path_template_rank_queen = path_tmpl_birck_rank + 'rank_queen.png'
path_template_rank_king = path_tmpl_birck_rank + 'rank_king.png'
path_template_rank_ace = path_tmpl_birck_rank + 'rank_ace.png'


Suit = Enum('Suits', 'Spade Heart Diamonds Club')
Cards = Enum(
    'Cards', 'Ace Two Three Four Five Six Seven Eight Nine Ten Eleven Twelf Thirteen')
