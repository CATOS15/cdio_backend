class DrawSquare:
    def __init__(self, color, thicc):
        self.color = color
        self.thicc = thicc


class TemplateInfo:
    def __init__(self, templ_image, threshold, width, height, drawSquare):
        self.templ_image = templ_image
        self.threshold = threshold
        self.width = width
        self.height = height
        self.drawSquare = drawSquare

    # def compare_template(self, washed_img):                        
    #     flipped = cv2.bitwise_not(self.templ_image)
    #     blur = cv2.GaussianBlur(flipped, (5, 5), 0)
    #     ret, th = cv2.threshold(
    #         blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    #     cv2.imwrite(path_template_sp1.format(0), th)
    #     return cv2.matchTemplate(washed_img, th, template_match_alg)

        # return cv2.matchTemplate(washed_img, self.templ_image, g_match_alg)


class Flow:
    def __init__(self, cb_wash, cb_contour, cb_cut_suit_rank, cb_compare_by_template):
        self.cb_wash = cb_wash
        self.cb_contour = cb_contour
        self.cb_cut_suit_rank = cb_cut_suit_rank
        # self.cb_resolution = cb_resolution
        self.cb_compare_by_template = cb_compare_by_template

    
    def execute_wash(self, ready_img, alg1):
        return self.cb_wash(ready_img, alg1)

        
    def execute_contour(self, alg1, alg2, img_thresh, img_color=None):
        return self.cb_contour(alg1, alg2, img_thresh,  img_color)

    def execute_cut_suit_rank(self, img_contours, alg1, alg2):
        return self.cb_cut_suit_rank(img_contours, alg1, alg2)

    
    #Implement resolution here
    # def execute_resolution(self, )
    
    def execute_compare_by_template(self, cards, ideal_image):
        return self.cb_compare_by_template(cards, ideal_image)



class Flow_ml:
    def __init__(self, cb_img_cut, cb_cut_columns, cb_ml_execute):
        self.cb_ml_execute = cb_ml_execute
        self.cb_img_cut = cb_img_cut
        self.cb_cut_columns = cb_cut_columns

    def execute_ml_single_img(self, img):
        return self.cb_ml_execute(img)

    def execute_img_cut(self, api_img):
        return self.cb_cut_columns(api_img)
    
    def execute_img_columns(self, img_tableau):
        return self.cb_cut_columns(img_tableau)


#either suit or rank, type: rank/suit, value = actual value
class TemplateType:
    def __init__(self, img, type, value, threshold):
        self.img = img
        self.type = type
        self.value = value
        self.threshold = threshold


    def suit_match(self, type):
        return self.type == type
    
    def higher_threshold(self, threshold):
        return self.type_threshold < threshold

    def add_success(self, contour):
        self.contour = contour


#add slot?
class Card:
    def __init__(self, suit, rank, suit_threshold, rank_threshold):
        self.suit = suit
        self.rank = rank
        self.suit_threshold = suit_threshold
        self.rank_threshold = rank_threshold

    def __str__(self):
        to_return = ""
        if self.rank == None and self.suit == None:
            return 'no appropriate matches for card found'

        if self.suit == None:
            to_return += 'suit: None' 
        else:
             to_return += 'suit: ' + self.suit.name
        
        if self.rank == None:
            to_return += '\trank: None'
        else:
            to_return += '\trank ' + self.rank.name
        
        if self.rank_threshold == None:
            to_return += '\trank_threshold: None'
        else:
            to_return += '\trank_threshold: ' + str(round(self.rank_threshold,4))
        
        if self.suit_threshold == None:
            to_return += '\tsuit_threshold: None'
        else:
            to_return += '\tsuit_threshold: ' + str(round(self.suit_threshold, 4))

        return to_return
    
    def __eq__(self, other):
    return self.suit==other.suit\
           and self.rank==other.rank


    def __hash__(self):
    return hash(('suit', self.suit,
                 'rank', self.rank))