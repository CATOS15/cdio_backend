import cv2
import unittest
import image_processing.flows as flows
import tests.birck.g_tests_shared as shared
# import image_processing.debugging as debugging
import image_processing.img_resolution as resolution
import image_processing.g_img as g_img


class TestIntegration(unittest.TestCase):
    def _best_match(self, current, contendor):
        if current == -1:
            return contendor
        elif contendor < current:
            return contendor
        else:
            return current

    def test_integration_waste(self):
        tmpl_bin_inv = resolution.bin_invert_templates(g_img.g_templates)
        for i, col_img in enumerate(shared.colored_imgs):
            card_contours = []
            washed = flows.flow_waste.execute_wash(col_img, cv2.THRESH_BINARY)
            contours = flows.flow_waste.execute_contour(cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=washed, img_color=col_img)
            
            for cunt in contours:
                card_contours.append(flows.flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

            cuts = flows.flow_waste.execute_cut_suit_rank(card_contours, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            match_results = []

            for card in cuts:
                if len(card['suits_numbers']) != 0:
                    s = flows.flow_waste.execute_compare_by_template(card, tmpl_bin_inv)
                    match_results.append(s)
            for x in match_results:
                print(x)                     
                    
if __name__ == '__main__':
    unittest.main()


