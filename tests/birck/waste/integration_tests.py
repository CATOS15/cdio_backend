import cv2
import unittest
import image_processing.flows as flows
import tests.birck.g_tests_shared as shared
# import image_processing.debugging as debugging


class TestIntegration(unittest.TestCase):
    def _best_match(self, current, contendor):
        if current == -1:
            return contendor
        elif contendor < current:
            return contendor
        else:
            return current

    def test_integration_suit_rank(self):
        for i, col_img in enumerate(shared.colored_imgs):
            card_contours = []
            washed = flows.flow_waste.execute_wash(col_img, cv2.THRESH_BINARY)
            contours = flows.flow_waste.execute_contour(cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, img_thresh=washed, img_color=col_img)
            for cunt in contours:
                card_contours.append(flows.flow_waste.execute_wash(cunt, cv2.THRESH_BINARY))

            cuts = flows.flow_waste.execute_cut_suit_rank(card_contours, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            

            for i, suit_rank in enumerate(shared.bin_suit_rank_templates):
                rank_template = suit_rank[0]
                suit_template = suit_rank[1]
                best_rank_match = -1
                best_suit_match = -1
                for cut in cuts:
                    if len(cut['suits_numbers']) != 0:
                        for suit_rank_cut in cut['suits_numbers']:
                            foo = cv2.matchShapes(rank_template, suit_rank_cut, cv2.CONTOURS_MATCH_I2, None)
                            best_rank_match = self._best_match(best_rank_match, foo)
                            best_suit_match = self._best_match(best_suit_match, cv2.matchShapes(suit_template, suit_rank_cut, cv2.CONTOURS_MATCH_I2, None))
                # test match here
                if (best_suit_match) < 1:
                    print(f'best_rank: {best_rank_match:.3f} \tbest_suit: {best_suit_match:.3f}')                
                    
if __name__ == '__main__':
    unittest.main()


