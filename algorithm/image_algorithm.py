from enum import Enum

class suit(Enum):
    DIAMOND = 1
    HEART = 2
    SPADE = 3
    CLUBS = 4

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

class Fountain:
    def __init__(self, count, suit):
        self.count = count
        self.suit = suit

class Moves:
    def __init__(self, cardFrom, toStack, description):
        self.cardFrom = cardFrom
        self.toStack = toStack
        self.description = description

#Ledig plads for en konge bliver Card(14, None)

fountains = [
    Fountain(1, suit.DIAMOND),
    Fountain(0, suit.HEART),
    Fountain(2, suit.SPADE),
    Fountain(0, suit.CLUBS)
]

stacks = [
    [Card(13, suit.SPADE), Card(12, suit.DIAMOND)],
    [Card(13, suit.CLUBS)],
    [Card(11, suit.CLUBS)],
    [Card(13, suit.HEART)],
    [Card(6, suit.HEART), Card(5, suit.CLUBS), Card(4, suit.HEART), Card(3, suit.SPADE)],
    [Card(8, suit.DIAMOND), Card(7, suit.SPADE)],
    [Card(10, suit.SPADE), Card(9, suit.HEART), Card(8, suit.CLUBS), Card(7, suit.HEART)]
]

cardpile = [Card(2, suit.DIAMOND)]

def rule_move_to_stack(cardFrom, cardTo):
    if cardFrom.number + 1 == cardTo.number and (((cardFrom.suit.value < 3 and cardTo.suit.value > 2) or (cardFrom.suit.value > 2 and cardTo.suit.value < 3)) or (cardTo.suit == None)):
        return True
    return False 

def rule_move_to_fountain(stack, cardFrom, fountain):
    topcard = stack[len(stack)-1]
    if (topcard.number == cardFrom.number and topcard.suit == cardFrom.suit):
        if fountain.count + 1 == cardFrom.number and fountain.suit == cardFrom.suit:
            return True
    return False

def get_moves():
    movesAvailable = []

    for fromIndex, fromStack in enumerate(stacks):
        for toIndex, toStack in enumerate(stacks):
            if fromStack != toStack:
                for card in fromStack:
                    if rule_move_to_stack(card, toStack[len(toStack)-1]):
                        movesAvailable.append(Moves(card, toStack, "Fra stack("+str(fromIndex+1)+") " + str(card.suit) + "(" + str(card.number) + ") til stack(" + str(toIndex+1) + ")"))
        for fountain in fountains:
            cardFrom = fromStack[len(fromStack)-1]
            if rule_move_to_fountain(fromStack, cardFrom, fountain):
                movesAvailable.append(Moves(cardFrom, fountain, "Fra stack("+str(fromIndex+1)+") " + str(cardFrom.suit) + "(" + str(cardFrom.number) + ") til fountain " + str(fountain.suit)))
    
    cardpile_topcard = cardpile[len(cardpile)-1]
    for toIndex, toStack in enumerate(stacks):
        if rule_move_to_stack(cardpile_topcard, toStack[len(toStack)-1]):
            movesAvailable.append(Moves(cardpile_topcard, toStack, "Fra cardpile " + str(cardpile_topcard.suit) + "(" + str(cardpile_topcard.number) + ") til stack(" + str(toIndex+1) + ")"))
    for fountain in fountains:
        if rule_move_to_fountain(cardpile, cardpile_topcard, fountain):
            movesAvailable.append(Moves(cardpile_topcard, fountain, "Fra cardpile " + str(cardpile_topcard.suit) + "(" + str(cardpile_topcard.number) + ") til fountain " + str(fountain.suit)))

    return movesAvailable

for x in get_moves():
    print(x.description)