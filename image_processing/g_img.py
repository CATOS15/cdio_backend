#Suits
path_template_suit_diamonds = 'templates/suit/3_diamonds_suit_template.png'
path_template_suit_hearts = 'templates/suit/3_hearts_suit.png'
path_tpe_suit_spades = ''
path_tpe_suit_clubs = ''

#Numbers Red
#tpe = template
path_tpe_number = 'examples/card2/3_diamonds_number_template.png'
path_tpe_ace = ''
path_tpe_2 = ''
path_tpe_3 = ''
path_tpe_4 = ''
path_tpe_5 = ''
path_tpe_6 = ''
path_tpe_7 = ''
path_tpe_8 = ''
path_tpe_9 = ''
path_tpe_10 = ''
path_tpe_jack = ''
path_tpe_queen = ''
path_tpe_king = ''

#Numbers Black <- hopefully we can delete this

#Testing
path_card = 'examples/card3/3_diamonds_hearts_whole.png' #this is input


img_color = cv2.imread(path_card)
img_grey = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

#Suits
template_suit_heart = cv2.imread(path_template_suit_hearts,0)
template_suit_diamonds = cv2.imread(path_template_suit_diamonds, 0)


#Numbers
template_number = cv2.imread(path_tpe_number, 0)


w_number, h_number = template_number.shape[::-1]
w_suit_diamonds, h_suit_diamonds = template_suit_diamonds.shape[::-1]
w_suit_heart, h_suit_heart = template_suit_heart.shape[::-1]


#Algorithm
suit_heart_match = cv2.matchTemplate(img_grey, template_suit_heart, cv2.TM_CCOEFF_NORMED)
suit_diamonds_match = cv2.matchTemplate(img_grey, template_suit_diamonds,cv2.TM_CCOEFF_NORMED)
number_match = cv2.matchTemplate(img_grey, template_number, cv2.TM_CCOEFF_NORMED)
