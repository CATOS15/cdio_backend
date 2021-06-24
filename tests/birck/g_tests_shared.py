#Gruppe 15
#Christian Frost s184140
#Mikkel Lindtner s205421 
#Nikolai Stein s205469
#Oliver Christensen s176352
#Søren Andersen s182881
#Tobias Kristensen s195458

import cv2
# import image_processing.debugging as debugging
import image_processing.img_wash as wash


# ideal threshold is suffix on each path
path_eight_diamond_131 = "tests/birck/full_deck_ground_truth/waste_eight_diamond_131.png"
path_eight_diamond_132 = "tests/birck/full_deck_ground_truth/waste_eight_diamond_132.png"
path_eight_heart_160 = "tests/birck/full_deck_ground_truth/waste_eight_heart_160.png"
path_king_diamond_128 = "tests/birck/full_deck_ground_truth/waste_king_diamond_128.png"
path_queen_club_180 = "tests/birck/full_deck_ground_truth/waste_queen_club_180.png"
path_two_diamond_190 = "tests/birck/full_deck_ground_truth/waste_two_diamond_190.png"

path_mask_eight_diamond_131 = "tests/birck/masked_ground_truth/eight_diamond_131.png"
path_mask_eight_diamond_132 = "tests/birck/masked_ground_truth/eight_diamond_132.png"
path_mask_eight_heart_160 = "tests/birck/masked_ground_truth/eight_heart_160.png"
path_mask_king_diamond_128 = "tests/birck/masked_ground_truth/king_diamond_128.png"
path_mask_queen_club_180 = "tests/birck/masked_ground_truth/queen_club_180_unsure.png"
path_mask_two_diamond_190 = "tests/birck/masked_ground_truth/two_diamond_190.png"

path_shape_eight_diamond_131 = "tests/birck/contour_ground_truth/shape_waste_eight_diamond_131.png"
path_shape_eight_diamond_131_cardback = "tests/birck/contour_ground_truth/shape_waste_eight_diamond_131_cardback.png"
path_shape_eight_heart_160 = "tests/birck/contour_ground_truth/shape_waste_eight_heart_160.png"
path_shape_eight_heart_160_cardback = "tests/birck/contour_ground_truth/shape_waste_eight_heart_160_cardback.png"
path_shape_king_diamond_128 = "tests/birck/contour_ground_truth/shape_waste_king_diamond_128.png"
path_shape_king_diamond_128_cardback = "tests/birck/contour_ground_truth/shape_waste_king_diamond_128_cardback.png"
path_shape_two_diamond_190 = "tests/birck/contour_ground_truth/shape_waste_two_diamond_190.png"
path_shape_two_diamond_190_cardback = "tests/birck/contour_ground_truth/shape_waste_two_diamond_190_cardback.png"

path_eight_diamond_131_template_rank = "tests/birck/cut_suit_rank_templates/waste_eight_diamond_131_template_rank.png"
path_eight_diamond_131_template_suit = "tests/birck/cut_suit_rank_templates/waste_eight_diamond_131_template_suit.png"
path_eight_diamond_132_template_rank = "tests/birck/cut_suit_rank_templates/waste_eight_diamond_132_template_rank.png"
path_eight_diamond_132_template_suit = "tests/birck/cut_suit_rank_templates/waste_eight_diamond_132_template_suit.png"
path_eight_heart_160_template_rank = "tests/birck/cut_suit_rank_templates/waste_eight_heart_160_template_rank.png"
path_eight_heart_160_template_suit = "tests/birck/cut_suit_rank_templates/waste_eight_heart_160_template_suit.png"
path_king_diamond_128_template_rank = "tests/birck/cut_suit_rank_templates/waste_king_diamond_128_template_rank.png"
path_king_diamond_128_template_suit = "tests/birck/cut_suit_rank_templates/waste_king_diamond_128_template_suit.png"
path_queen_club_180_template_rank = "tests/birck/cut_suit_rank_templates/waste_queen_club_180_template_rank.png"
path_queen_club_180_template_suit = "tests/birck/cut_suit_rank_templates/waste_queen_club_180_template_suit.png"
path_two_diamond_190_template_rank = "tests/birck/cut_suit_rank_templates/waste_two_diamond_190_template_rank.png"
path_two_diamond_190_template_suit = "tests/birck/cut_suit_rank_templates/waste_two_diamond_190_template_suit.png"



path_eight_diamond_131_template_rank_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_eight_diamond_131_template_rank_bin.png"
path_eight_diamond_131_template_suit_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_eight_diamond_131_template_suit_bin.png"
path_eight_diamond_132_template_rank_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_eight_diamond_132_template_rank_bin.png"
path_eight_diamond_132_template_suit_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_eight_diamond_132_template_suit_bin.png"
path_eight_heart_160_template_rank_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_eight_heart_160_template_rank_bin.png"
path_eight_heart_160_template_suit_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_eight_heart_160_template_suit_bin.png"
path_king_diamond_128_template_rank_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_king_diamond_128_template_rank_bin.png"
path_king_diamond_128_template_suit_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_king_diamond_128_template_suit_bin.png"
# path_queen_diamond_190_template_rank_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_queen_diamond_190_template_rank_bin.png"
# path_queen_diamond_190_template_suit_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_queen_diamond_190_template_suit_bin.png"
path_two_diamond_190_template_rank_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_two_diamond_190_template_rank_bin.png"
path_two_diamond_190_template_suit_bin = "tests/birck/cut_suit_rank_templates/bin_templates/waste_two_diamond_190_template_suit_bin.png"


path_eight_diamond_131_contour_col1 = "tests/birck/contour_ground_truth/contour_col_ground_truth/eight_diamond_131_contour_col1.png"
path_eight_diamond_131_contour_col2 = "tests/birck/contour_ground_truth/contour_col_ground_truth/eight_diamond_131_contour_col2.png"
path_eight_diamond_132_contour_col1 = "tests/birck/contour_ground_truth/contour_col_ground_truth/eight_diamond_132_contour_col1.png"
path_eight_diamond_132_contour_col2 = "tests/birck/contour_ground_truth/contour_col_ground_truth/eight_diamond_132_contour_col2.png"
path_eight_heart_160_contour_col1 = "tests/birck/contour_ground_truth/contour_col_ground_truth/eight_heart_160_contour_col1.png"
path_eight_heart_160_contour_col2 = "tests/birck/contour_ground_truth/contour_col_ground_truth/eight_heart_160_contour_col2.png"
path_king_diamond_128_contour_col1 = "tests/birck/contour_ground_truth/contour_col_ground_truth/king_diamond_128_contour_col1.png"
path_king_diamond_128_contour_col2 = "tests/birck/contour_ground_truth/contour_col_ground_truth/king_diamond_128_contour_col2.png"
path_two_diamond_190_contour_col1 = "tests/birck/contour_ground_truth/contour_col_ground_truth/two_diamond_190_contour_col1.png"
path_two_diamond_190_contour_col2 = "tests/birck/contour_ground_truth/contour_col_ground_truth/two_diamond_190_contour_col2.png"




eight_diamond_131 = cv2.imread(path_eight_diamond_131, cv2.IMREAD_COLOR)
eight_diamond_132 = cv2.imread(path_eight_diamond_132, cv2.IMREAD_COLOR)
eight_heart_160 = cv2.imread(path_eight_heart_160, cv2.IMREAD_COLOR)
king_diamond_128 = cv2.imread(path_king_diamond_128, cv2.IMREAD_COLOR)
queen_club_180 = cv2.imread(path_queen_club_180, cv2.IMREAD_COLOR)
two_diamond_190 = cv2.imread(path_two_diamond_190, cv2.IMREAD_COLOR)

shape_eight_diamond_131 = cv2.imread(path_shape_eight_diamond_131, cv2.IMREAD_GRAYSCALE)
shape_eight_diamond_131_cardback = cv2.imread(path_shape_eight_diamond_131_cardback, cv2.IMREAD_GRAYSCALE)
shape_eight_heart_160 = cv2.imread(path_shape_eight_heart_160, cv2.IMREAD_GRAYSCALE)
shape_eight_heart_160_cardback = cv2.imread(path_shape_eight_heart_160_cardback, cv2.IMREAD_GRAYSCALE)
shape_king_diamond_128 = cv2.imread(path_shape_king_diamond_128, cv2.IMREAD_GRAYSCALE)
shape_king_diamond_128_cardback = cv2.imread(path_shape_king_diamond_128_cardback, cv2.IMREAD_GRAYSCALE)
shape_two_diamond_190 = cv2.imread(path_shape_two_diamond_190, cv2.IMREAD_GRAYSCALE)
shape_two_diamond_190_cardback = cv2.imread(path_shape_two_diamond_190, cv2.IMREAD_GRAYSCALE)

mask_eight_diamond_131 = cv2.imread(path_mask_eight_diamond_131, cv2.IMREAD_GRAYSCALE)
mask_eight_diamond_132 = cv2.imread(path_mask_eight_diamond_132, cv2.IMREAD_GRAYSCALE)
mask_eight_heart_160 = cv2.imread(path_mask_eight_heart_160, cv2.IMREAD_GRAYSCALE)
mask_king_diamond_128 = cv2.imread(path_mask_king_diamond_128, cv2.IMREAD_GRAYSCALE)
mask_queen_club_180 = cv2.imread(path_mask_queen_club_180, cv2.IMREAD_GRAYSCALE)
mask_two_diamond_190 = cv2.imread(path_mask_two_diamond_190, cv2.IMREAD_GRAYSCALE)

template_eight_diamond_131_rank = cv2.imread(path_eight_diamond_131_template_rank, cv2.IMREAD_COLOR)
template_eight_diamond_131_suit = cv2.imread(path_eight_diamond_131_template_suit, cv2.IMREAD_COLOR)
template_eight_diamond_132_rank = cv2.imread(path_eight_diamond_132_template_rank, cv2.IMREAD_COLOR)
template_eight_diamond_132_suit = cv2.imread(path_eight_diamond_132_template_suit, cv2.IMREAD_COLOR)
template_eight_heart_160_rank = cv2.imread(path_eight_heart_160_template_rank, cv2.IMREAD_COLOR)
template_eight_heart_160_suit = cv2.imread(path_eight_heart_160_template_suit, cv2.IMREAD_COLOR)
template_king_diamond_128_rank = cv2.imread(path_king_diamond_128_template_rank, cv2.IMREAD_COLOR)
template_king_diamond_128_suit = cv2.imread(path_king_diamond_128_template_suit, cv2.IMREAD_COLOR)
# template_queen_club_180_rank = cv2.imread(path_queen_club_180_template_rank, cv2.IMREAD_COLOR)
# template_queen_club_180_suit = cv2.imread(path_queen_club_180_template_suit, cv2.IMREAD_COLOR)
template_two_diamond_190_rank = cv2.imread(path_two_diamond_190_template_rank, cv2.IMREAD_COLOR)
template_two_diamond_190_suit = cv2.imread(path_two_diamond_190_template_suit, cv2.IMREAD_COLOR)

template_eight_diamond_131_rank_bin = cv2.imread(path_eight_diamond_131_template_rank_bin, cv2.IMREAD_GRAYSCALE)
template_eight_diamond_131_suit_bin = cv2.imread(path_eight_diamond_131_template_suit_bin, cv2.IMREAD_GRAYSCALE)
template_eight_diamond_132_rank_bin = cv2.imread(path_eight_diamond_131_template_rank_bin, cv2.IMREAD_GRAYSCALE)
template_eight_diamond_132_suit_bin = cv2.imread(path_eight_diamond_132_template_suit_bin, cv2.IMREAD_GRAYSCALE)
template_eight_heart_160_rank_bin = cv2.imread(path_eight_heart_160_template_rank_bin, cv2.IMREAD_GRAYSCALE)
template_eight_heart_160_suit_bin = cv2.imread(path_eight_heart_160_template_suit_bin, cv2.IMREAD_GRAYSCALE)
template_king_diamond_128_rank_bin = cv2.imread(path_king_diamond_128_template_rank_bin, cv2.IMREAD_GRAYSCALE)
template_king_diamond_128_suit_bin = cv2.imread(path_king_diamond_128_template_suit_bin, cv2.IMREAD_GRAYSCALE)
template_two_diamond_190_rank_bin = cv2.imread(path_two_diamond_190_template_rank_bin, cv2.IMREAD_GRAYSCALE)
template_two_diamond_190_suit_bin = cv2.imread(path_two_diamond_190_template_suit_bin, cv2.IMREAD_GRAYSCALE)

contour_eight_diamond_131_col1 = cv2.imread(path_eight_diamond_131_contour_col1, cv2.IMREAD_GRAYSCALE)
contour_eight_diamond_131_col2 = cv2.imread(path_eight_diamond_131_contour_col2, cv2.IMREAD_GRAYSCALE)
contour_eight_diamond_132_col1 = cv2.imread(path_eight_diamond_132_contour_col1, cv2.IMREAD_GRAYSCALE)
contour_eight_diamond_132_col2 = cv2.imread(path_eight_diamond_132_contour_col2, cv2.IMREAD_GRAYSCALE)
contour_eight_heart_160_col1 = cv2.imread(path_eight_heart_160_contour_col1, cv2.IMREAD_GRAYSCALE)
contour_eight_heart_160_col2 = cv2.imread(path_eight_heart_160_contour_col2, cv2.IMREAD_GRAYSCALE)
contour_king_diamond_128_col1 = cv2.imread(path_king_diamond_128_contour_col1, cv2.IMREAD_GRAYSCALE)
contour_king_diamond_128_col2 = cv2.imread(path_king_diamond_128_contour_col2, cv2.IMREAD_GRAYSCALE)
contour_two_diamond_190_col1 = cv2.imread(path_two_diamond_190_contour_col1, cv2.IMREAD_GRAYSCALE)
contour_two_diamond_190_col2 = cv2.imread(path_two_diamond_190_contour_col2, cv2.IMREAD_GRAYSCALE)


# colored and mask must have identitical lengths
colored_imgs = [eight_diamond_131, eight_diamond_132, eight_heart_160, king_diamond_128,
                two_diamond_190]

mask_imgs = [mask_eight_diamond_131, mask_eight_diamond_132, mask_eight_heart_160,
             mask_king_diamond_128, mask_two_diamond_190]

# Combine contours
shapes_eight_diamond_131 = [shape_eight_diamond_131_cardback, shape_eight_diamond_131]
shapes_eight_heart_160 = [shape_eight_heart_160_cardback, shape_eight_heart_160]
shapes_king_diamond_128 = [shape_king_diamond_128_cardback, shape_king_diamond_128]
shapes_two_diamond_190 = [shape_two_diamond_190_cardback, shape_two_diamond_190]

shapes = [shapes_eight_diamond_131, shapes_eight_heart_160, shapes_king_diamond_128, shapes_two_diamond_190]
contour_images = [mask_eight_diamond_131, mask_eight_heart_160, mask_king_diamond_128, mask_two_diamond_190]

# Suit rank array in color
template_eight_diamond_131 = [template_eight_diamond_131_rank, template_eight_diamond_131_suit]
template_eight_diamond_132 = [template_eight_diamond_132_rank, template_eight_diamond_132_suit]
template_eight_heart_160 =  [template_eight_heart_160_rank, template_eight_heart_160_suit]
template_king_diamond_128 = [template_king_diamond_128_rank, template_king_diamond_128_suit]
# template_queen_club_180 = [template_queen_club_180_rank, template_queen_club_180_suit]
template_two_diamond_190 = [template_two_diamond_190_rank, template_two_diamond_190_suit]
color_suit_rank_templates = [template_eight_diamond_131,template_eight_diamond_132,template_eight_heart_160,
                        template_king_diamond_128,template_two_diamond_190]

# Suit rank array in bin
template_eight_diamond_131_bin = [template_eight_diamond_131_rank_bin, template_eight_diamond_131_suit_bin]
template_eight_diamond_132_bin = [template_eight_diamond_132_rank_bin, template_eight_diamond_132_suit_bin]
template_eight_heart_160_bin = [template_eight_heart_160_rank_bin, template_eight_heart_160_suit_bin]
template_king_diamond_128_bin = [template_king_diamond_128_rank_bin, template_king_diamond_128_suit_bin]
template_two_diamond_190_bin = [template_two_diamond_190_rank_bin,template_two_diamond_190_suit_bin]

bin_suit_rank_templates = [template_eight_diamond_131_bin,template_eight_diamond_132_bin,
template_eight_heart_160_bin,template_king_diamond_128_bin,template_two_diamond_190_bin]


# Contour columns
contour_cols_eight_diamond_131 = [contour_eight_diamond_131_col1, contour_eight_diamond_131_col2]
contour_cols_eight_diamond_132 = [contour_eight_diamond_132_col1, contour_eight_diamond_132_col2]
contour_cols_eight_heart_160 = [contour_eight_heart_160_col1, contour_eight_heart_160_col2]
contour_cols_king_diamond_128 = [contour_king_diamond_128_col1,contour_king_diamond_128_col2]
contour_cols_two_diamond_190 = [contour_two_diamond_190_col1,contour_two_diamond_190_col2]
contours_cols_collected = [contour_cols_eight_diamond_131, contour_cols_eight_diamond_132, contour_cols_eight_heart_160, contour_cols_king_diamond_128, contour_cols_two_diamond_190]




def test_save_template_images():
    file_path = "tests/birck/cut_suit_rank_templates/bin_templates/double_washed_templates_{}.png"
    washed_suit_rank_template = []
    for i, x in enumerate(color_suit_rank_templates):
        #instead of using otsu wash we should have manually made satisfactory bin images
        foo = wash.otsu_wash(x, cv2.THRESH_BINARY)

        cv2.imwrite(file_path.format(str(i)), foo)
        # washed_suit_rank_template.append(cv2.threshold())