import image_processing.objects as objects
import image_processing.img_wash as wash
import image_processing.img_contour as contour
import image_processing.img_cut_suit_rank as cut_suit_rank
import image_processing.img_compare as compare

flow_waste = objects.Flow(cb_wash=wash.otsu_wash, cb_contour=contour.contour_approximation,
                  cb_cut_suit_rank=cut_suit_rank.find_by_hierachy, cb_compare_by_template=compare.compare_ranksuit)