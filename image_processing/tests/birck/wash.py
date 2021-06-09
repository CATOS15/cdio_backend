from typing import Optional
import unittest
import numpy as np
import cv2
import image_processing.objects as objects
import image_processing.img_wash as wash

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

    colored_imgs = [eight_diamond_131, eight_diamond_132, eight_heart_160, king_diamond_128,
                    queen_club_180, two_diamond_190]
    mask_imgs = [mask_eight_diamond_131, mask_eight_diamond_132, mask_eight_heart_160,
                 mask_king_diamond_128, mask_queen_club_180, mask_two_diamond_190]

    wash_strategy = cv2.THRESH_BINARY

    def same_resolution(self, img1, img2):
        height = 0
        width = 1
        return (img1.shape[height] == img2.shape[height], img1.shape[width] == img2.shape[width])

    #Ensure that bin images and colored images has the same resolution
    def test_resolution_foo(self):
        sheight = "height"
        swidth = "width"
        for i, x in enumerate(TestWash.colored_imgs):
            test_resolution = self.same_resolution(x, TestWash.mask_imgs[i])
            self.assertEqual(True, test_resolution[0], "dimensions error {}: {} & mask ".format(sheight, str(x)))
            self.assertEqual(True, test_resolution[1], "dimensions error {}: {} & mask ".format(swidth, str(x)))


    def test_quick(self):
        self.assertEqual(sum([2, 3]), 5, "6 is nice")

    def test_wash_otsu_simple(self):
        wash_results = []
        wash_results.append(self.otsu_simple.execute_wash(eight_diamond_131, TestWash.wash_strategy))
        # wash_results.append(self.otsu_simple.execute_wash(eight_diamond_132, TestWash.wash_strategy))
        # wash_results.append(self.otsu_simple.execute_wash(eight_heart_160, TestWash.wash_strategy))
        # wash_results.append(self.otsu_simple.execute_wash(king_diamond_128, TestWash.wash_strategy))
        # wash_results.append(self.otsu_simple.execute_wash(queen_club_180, TestWash.wash_strategy))
        # wash_results.append(self.otsu_simple.execute_wash(two_diamond_190, TestWash.wash_strategy))

        pearson_results = []
        tanimoto_results = []

        for i, threshold_img in enumerate(wash_results):
            pearson_results.append(pearson(threshold_img, TestWash.mask_imgs[i]))
            # tanimoto_results.append(tanimoto(threshold_img, TestWash.optimal_results[i]))

        print(pearson_results)

        self.assertEqual(True, True, "well thats good")
        # Test this smh


def pearson(img_test, ground_truth_mask):
    return np.corrcoef(img_test, ground_truth_mask)


def tanimoto(img_test, ground_truth_mask):
    inter = img_test.intersection(ground_truth_mask)
    union = img_test.union(ground_truth_mask)

    sum_inter = sum(inter)
    sum_union = sum(union)
    return sum_inter/sum_union


# class TestDimensions(unittest.TestCase):


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
