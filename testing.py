from enum import Enum
import copy
import json
import random

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

stacksNumber = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
fountainNumber = [
    [],
    [],
    [],
    [],
]
cardPileNumber = []

allNumbers = []

for x in range(1,5):
    for y in range(1,14):
        allNumbers.append(Card(y,x))
for x in range(0,len(stacksNumber)):
    exist = True

    while exist == True:
        numb = random.randrange(1,13)
        value = random.randrange(1,4)
        currentCard = Card(numb,value)
        for y in allNumbers:
            if currentCard.number == y.number and currentCard.suit== y.suit:
                allNumbers.remove(y)
                stacksNumber[x].append(y)
                exist = False
numb = random.randrange(1,13)
value = random.randrange(1,4)
currentCard = Card(numb,value)
for y in allNumbers:
    if currentCard.number == y.number and currentCard.suit== y.suit:
        allNumbers.remove(y)
        cardPileNumber.append(y)
        exist = False                 

                    

# print(stacksNumber)

for h in stacksNumber:
    print("Stack - Number: " + str(h[0].number) + " Suit: " +  str(h[0].suit))
    # print(h)
print("CardPile - number: " + str(cardPileNumber[0].number) + " suit: " + str(cardPileNumber[0].suit))

data_solitaire = {
        'stacks': [
            [
                {'number': random.randrange(1,13), 'suit': 3}
            ],
            [
                {'number': 12, 'suit': 2}
            ],
            [
                {'number': 11, 'suit': 3}
            ],
            [
                {'number': 11, 'suit': 4}
            ],
            [
                {'number': 12, 'suit': 1}
            ],
            [
                {'number': 6, 'suit': 1}
            ],
            [
                {'number': 7, 'suit': 1}
            ],
        ],
        'fountains': [
            {'number': 1, 'suit': 1},
            {'number': 1, 'suit': 2},
            {'number': 0, 'suit': 3},
            {'number': 1, 'suit': 4}
        ],
        'cardpile': [
            {'number': 8, 'suit': 2}
        ],
    }
# print(data_solitaire)