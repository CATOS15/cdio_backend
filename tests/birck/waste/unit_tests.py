import cv2
import unittest
import numpy as np
import tests.birck.test_objects as tobj
import image_processing.img_wash as wash
import image_processing.objects as objects
import tests.birck.g_tests_shared as shared
from image_processing.img_contour import contour_approximation

# Birck Wash Tests
class TestContur(unittest.TestCase):
    otsu_capprox = objects.Flow(cb_wash=wash.otsu_wash, cb_contour=contour_approximation, cb_cut_suit_rank=None, cb_compare_by_template=None)

    cmatches = []
    cmatches.append(tobj.ContourMatch("mask_eight_diamond_131", shared.mask_eight_diamond_131))
    cmatches.append(tobj.ContourMatch("mask_eight_diamond_132", shared.mask_eight_diamond_132))
    cmatches.append(tobj.ContourMatch("mask_eight_heart_160", shared.mask_eight_heart_160))
    cmatches.append(tobj.ContourMatch("mask_king_diamond_128", shared.mask_king_diamond_128))
    cmatches.append(tobj.ContourMatch("mask_two_diamond", shared.mask_two_diamond_190))

    # uses I2
    # https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#gaf2b97a230b51856d09a2d934b78c015f
    # https://learnopencv.com/shape-matching-using-hu-moments-c-python/
    def test_contour_approximation(self):
        contours_result = []
        for cmatch in self.cmatches:
            contours = self.otsu_capprox.execute_contour(cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, cmatch.ground_truth)
            boundingBoxes = [cv2.boundingRect(c) for c in contours]
            (cnts_sorted, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b: b[1][0], reverse=False))
            cnt_deck = cnts_sorted[0]  # deck
            cnt_card = cnts_sorted[1]  # card
            cmatch.find_best_result(cv2.matchShapes(cmatch.ground_truth, cnt_deck, cv2.CONTOURS_MATCH_I2, None), True)
            cmatch.find_best_result(cv2.matchShapes(cmatch.ground_truth, cnt_card, cv2.CONTOURS_MATCH_I2, None), False)
            contours_result.append(cmatch)
        for result in contours_result:
            print(result)

# Tests washing
class TestWash(unittest.TestCase):
    otsu_simple = objects.Flow(cb_wash=wash.otsu_wash, cb_contour=None,
                               cb_cut_suit_rank=None, cb_compare_by_template=None)

    wash_strategy = cv2.THRESH_BINARY

    def same_resolution(self, img1, img2):
        height = 0
        width = 1
        return (img1.shape[height] == img2.shape[height], img1.shape[width] == img2.shape[width])

    # Ensure that bin images and colored images has the same resolution
    def test_resolution_mask_color(self):
        sheight = "height"
        swidth = "width"
        for i, color_img in enumerate(shared.colored_imgs):
            test_wash = self.otsu_simple.cb_wash(color_img, TestWash.wash_strategy)
            test_wash_resolution = self.same_resolution(color_img, test_wash)
            test_resolution = self.same_resolution(color_img, shared.mask_imgs[i])

            self.assertEqual(True, test_resolution[0], "dimensions error {}: {} & mask ".format(sheight, str(color_img)))
            self.assertEqual(True, test_resolution[1], "dimensions error {}: {} & mask ".format(swidth, str(color_img)))
            self.assertEqual(True, test_wash_resolution[0], "dimensions error {}: {} & mask ".format(sheight, str(color_img)))
            self.assertEqual(True, test_wash_resolution[1], "dimensions error {}: {} & mask ".format(swidth, str(color_img)))

    def _wash_array(self, cb_wash):
        results = []
        for x in shared.colored_imgs:
            results.append(cb_wash(x, TestWash.wash_strategy))
        return results

    def test_wash_otsu_simple(self):
        pearson_results = []
        accuracy_results = []
        tanimoto_results = []
        wash_results = self._wash_array(self.otsu_simple.cb_wash)

        for i, threshold_img in enumerate(wash_results):
            pearson_results.append(pearson_corr_coeff(threshold_img, shared.mask_imgs[i]))
            accuracy_results.append(accuracy(threshold_img, shared.mask_imgs[i]))
            tanimoto_results.append(tanimoto_corr_coeff(threshold_img, shared.mask_imgs[i]))

        print(pearson_results)
        print(tanimoto_results)
        print(accuracy_results)

# pearson correlation coefficient


def pearson_corr_coeff(img_test, ground_truth_mask):
    img_test_average = np.mean(img_test)
    ground_truth_mask_average = np.mean(ground_truth_mask)
    numerator = np.sum((img_test - img_test_average) * (ground_truth_mask - ground_truth_mask_average))
    denomitor_img = np.sqrt(np.sum((img_test - img_test_average)**2))
    denomitor_ground_truth = np.sqrt(np.sum((ground_truth_mask - ground_truth_mask_average)**2))

    return numerator / (denomitor_img * denomitor_ground_truth)


# tanimoto's correlation correficient
def tanimoto_corr_coeff(img, ground_truth_mask):
    numerator = np.sum(np.bitwise_and(img, ground_truth_mask))
    denomiter = np.sum(np.bitwise_or(img, ground_truth_mask))

    return numerator / denomiter


# binary accuracy: https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers (see accuracy)
def accuracy(img_test, ground_truth_mask):
    m_00 = 0
    m_10 = 0
    m_01 = 0
    m_11 = 0

    white = 255
    black = 0
    for i, row in enumerate(img_test):
        for j, pixel in enumerate(row):
            if pixel == black and ground_truth_mask[i][j] == black:
                m_00 += 1
            elif pixel == white and ground_truth_mask[i][j] == white:
                m_10 += 1
            elif pixel == black and ground_truth_mask[i][j] == white:
                m_01 += 1
            elif pixel == white and ground_truth_mask[i][j] == white:
                m_11 += 1

    return (m_11 + m_00) / (m_10 + m_01 + m_11 + m_00)


if __name__ == '__main__':
    unittest.main()


# Contours
    # https://en.wikipedia.org/wiki/Image_moment
    # Contour sorting: https://www.pyimagesearch.com/2015/04/20/sorting-contours-using-python-and-opencv/


# Otzu / washing testing
    # https://link.springer.com/chapter/10.1007/978-3-319-39393-3_4
    # Pearson correlation
    # https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#Sample_size
    # coefficient https://stackabuse.com/calculating-pearson-correlation-coefficient-in-python-with-numpy
    # Tanimotos
    # https://en.wikipedia.org/wiki/Jaccard_index#:~:text=Tanimoto%20goes%20on%20to%20define,be%20similar%20to%20a%20third.
    # threshold
    # https://pinetools.com/threshold-image

    # ground_truth_mask
    # Choose an image
    # Find global threshold with greyscale using pinetools

    # SCIPY
    # pearson: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html
