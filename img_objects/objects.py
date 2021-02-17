from enum import Enum
Suit = Enum('Suits', 'Spade Heart Diamonds Club')
#Ace: 0, king: 12
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

#tablue consists of 7 columns
#foundataion conists of 4 columns
#waste consists of 1 column
#stock will be ignored
class Column:
    def __init__(self, cards, size):
        self.cards = cards
        self.size = size

    def face_up_amount():
        face_up = 0
        for c in self.cards:
            if c.value > -1:
                face_up += 1
        return face_up
    
