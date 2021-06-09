from typing import Optional
import unittest
import numpy as np
import cv2
import image_processing.objects as objects
import image_processing.img_wash as wash
from scipy import stats


# Birck Wash Tests
# ideal threhsold is suffix on each path

path_eight_diamond_131 = "image_processing/tests/birck/full_deck_ground_truth/waste_eight_diamond_131.png"
path_eight_diamond_132 = "image_processing/tests/birck/full_deck_ground_truth/waste_eight_diamond_132.png"
path_eight_heart_160 = "image_processing/tests/birck/full_deck_ground_truth/waste_eight_heart_160.png"
path_king_diamond_128 = "image_processing/tests/birck/full_deck_ground_truth/waste_king_diamond_128.png"
path_queen_club_180 = "image_processing/tests/birck/full_deck_ground_truth/waste_queen_club_180.png"
path_two_diamond_190 = "image_processing/tests/birck/full_deck_ground_truth/waste_two_diamond_190.png"

path_mask_eight_diamond_131 = "image_processing/tests/birck/masked_ground_truth/eight_diamond_131.png"
path_mask_eight_diamond_132 = "image_processing/tests/birck/masked_ground_truth/eight_diamond_132.png"
path_mask_eight_heart_160 = "image_processing/tests/birck/masked_ground_truth/eight_heart_160.png"
path_mask_king_diamond_128 = "image_processing/tests/birck/masked_ground_truth/king_diamond_128.png"
path_mask_queen_club_180 = "image_processing/tests/birck/masked_ground_truth/queen_club_180_unsure.png"
path_mask_two_diamond_190 = "image_processing/tests/birck/masked_ground_truth/two_diamond_190.png"


eight_diamond_131 = cv2.imread(path_eight_diamond_131, cv2.IMREAD_COLOR)
eight_diamond_132 = cv2.imread(path_eight_diamond_132, cv2.IMREAD_COLOR)
eight_heart_160 = cv2.imread(path_eight_heart_160, cv2.IMREAD_COLOR)
king_diamond_128 = cv2.imread(path_king_diamond_128, cv2.IMREAD_COLOR)
queen_club_180 = cv2.imread(path_queen_club_180, cv2.IMREAD_COLOR)
two_diamond_190 = cv2.imread(path_two_diamond_190, cv2.IMREAD_COLOR)

mask_eight_diamond_131 = cv2.imread(path_mask_eight_diamond_131, cv2.IMREAD_GRAYSCALE)
mask_eight_diamond_132 = cv2.imread(path_mask_eight_diamond_132, cv2.IMREAD_GRAYSCALE)
mask_eight_heart_160 = cv2.imread(path_mask_eight_heart_160, cv2.IMREAD_GRAYSCALE)
mask_king_diamond_128 = cv2.imread(path_mask_king_diamond_128, cv2.IMREAD_GRAYSCALE)
mask_queen_club_180 = cv2.imread(path_mask_queen_club_180, cv2.IMREAD_GRAYSCALE)
mask_two_diamond_190 = cv2.imread(path_mask_two_diamond_190, cv2.IMREAD_GRAYSCALE)


class TestWash(unittest.TestCase):
    otsu_simple = objects.Flow(cb_wash=wash.otsu_wash, cb_contour=None,
                               cb_cut_suit_rank=None, cb_compare_by_template=None)

    # colored and mask must have identitical lengths
    colored_imgs = [eight_diamond_131, eight_diamond_132, eight_heart_160, king_diamond_128,
                    queen_club_180, two_diamond_190]

    mask_imgs = [mask_eight_diamond_131, mask_eight_diamond_132, mask_eight_heart_160,
                 mask_king_diamond_128, mask_queen_club_180, mask_two_diamond_190]

    wash_strategy = cv2.THRESH_BINARY

    def same_resolution(self, img1, img2):
        height = 0
        width = 1
        return (img1.shape[height] == img2.shape[height], img1.shape[width] == img2.shape[width])

    # Ensure that bin images and colored images has the same resolution
    def test_resolution_mask_color(self):
        sheight = "height"
        swidth = "width"
        for i, color_img in enumerate(TestWash.colored_imgs):
            test_wash = self.otsu_simple.cb_wash(color_img, TestWash.wash_strategy)
            test_wash_resolution = self.same_resolution(color_img, test_wash)
            test_resolution = self.same_resolution(color_img, TestWash.mask_imgs[i])

            self.assertEqual(True, test_resolution[0], "dimensions error {}: {} & mask ".format(sheight, str(color_img)))
            self.assertEqual(True, test_resolution[1], "dimensions error {}: {} & mask ".format(swidth, str(color_img)))
            self.assertEqual(True, test_wash_resolution[0], "dimensions error {}: {} & mask ".format(sheight, str(color_img)))
            self.assertEqual(True, test_wash_resolution[1], "dimensions error {}: {} & mask ".format(swidth, str(color_img)))
            

    def _wash_array(self, cb_wash):
        results = []
        for x in self.colored_imgs:
            results.append(cb_wash(x, TestWash.wash_strategy))
        return results

    # def test_wash_otsu_simple(self):
    #     pearson_results = []
    #     tanimoto_results = []
    #     wash_results = self._wash_array(self.otsu_simple.cb_wash)

    #     for i, threshold_img in enumerate(wash_results):
    #         pearson_results.append(pearson(threshold_img, TestWash.mask_imgs[i]))
    #         # tanimoto_results.append(tanimoto(threshold_img, TestWash.optimal_results[i]))

    #     print(pearson_results)



def pearson(img_test, ground_truth_mask):
    pearson_corr = []

    for i,row in enumerate(img_test):
        pea_corr, p_value = stats.pearsonr(img_test[i], ground_truth_mask[i])
        pearson_corr.append(pea_corr)

    return np.mean(pearson_corr)


    # return np.corrcoef(img_test, ground_truth_mask)


def tanimoto(img_test, ground_truth_mask):
    inter = img_test.intersection(ground_truth_mask)
    union = img_test.union(ground_truth_mask)

    sum_inter = sum(inter)
    sum_union = sum(union)
    return sum_inter/sum_union


if __name__ == '__main__':
    unittest.main()


# Otzu / washing testing
# https://link.springer.com/chapter/10.1007/978-3-319-39393-3_4
# Pearson correlation
    # coefficient https://stackabuse.com/calculating-pearson-correlation-coefficient-in-python-with-numpy
# Tanimotos
    # https://en.wikipedia.org/wiki/Jaccard_index#:~:text=Tanimoto%20goes%20on%20to%20define,be%20similar%20to%20a%20third.
# threshold
    # https://pinetools.com/threshold-image


# ground_truth_mask
    # Choose an image
    # Find global threshold with greyscale using pinetools


# TODO
# refactor Dict(colored_img_1:mask_img_1 ... )
