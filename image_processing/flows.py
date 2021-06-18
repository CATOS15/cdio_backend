import image_processing.img_wash as wash
import image_processing.objects as objects
import communication_layer.ml_alg as ml_alg
import ml_solitaire.cut_image as ml_cut_image
import image_processing.img_contour as contour
import image_processing.img_compare as compare
import image_processing.img_cut_suit_rank as cut_suit_rank


flow_waste = objects.Flow(cb_wash=wash.otsu_wash, cb_contour=contour.contour_approximation,
                          cb_cut_suit_rank=cut_suit_rank.find_by_hierachy, cb_compare_by_template=compare.compare_ranksuit)

flow_ml_subdivide_tableau = objects.Flow_ml(cb_img_cut=ml_cut_image.cut_img_cut_three,
                                            cb_cut_columns=ml_alg.opencv_ml_tableau_columns_color,
                                            cb_ml_execute=ml_alg.ml_map_alg)

opencv_flow_tableau = objects.Flow(cb_wash=wash.otsu_wash, cb_contour=contour.contours_cut_columns,
                                  cb_cut_suit_rank=cut_suit_rank.find_by_hierachy_less_noise, cb_compare_by_template=compare.compare_ranksuit)

