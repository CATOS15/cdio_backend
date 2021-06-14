import unittest
import image_processing.debugging as debugging
import tests.birck.g_tests_shared as shared
import image_processing.flows as flows
import cv2


class TestIntegration(unittest.TestCase):
    def test_integration_suit_rank(self):
  
        for col_img in shared.colored_imgs:
            card_contours = []
            washed = flows.flow_waste.execute_wash(col_img, cv2.THRESH_BINARY)
            contours = flows.flow_waste.execute_contour(cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, washed)
            for cunt in contours:
                card_contours.append(flows.flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

            cuts = flows.flow_waste.execute_cut_suit_rank(card_contours, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # test cuts here

    # def test_save_template_images(self):
    #     file_path = "tests/birck/cut_suit_rank_templates/bin_templates/bin_{}.png"
    #     washed_suit_rank_template = []
    #     for i, x in enumerate(suit_rank_templates):
    #         #instead of using otsu wash we should have manually made satisfactory bin images
    #         foo = wash.otsu_wash(x, cv2.THRESH_BINARY)
    #         cv2.imwrite(file_path.format(str(i)), foo)
    #         # washed_suit_rank_template.append(cv2.threshold())
