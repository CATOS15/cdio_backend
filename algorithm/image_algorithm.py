from enum import Enum
import copy

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
    def __init__(self, cardFrom, cardFromIndex, fromStack, toStack, description):
        self.cardFrom = cardFrom
        self.cardFromIndex = cardFromIndex
        self.fromStack = fromStack
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
    [Card(11, suit.HEART)],
    [Card(1, suit.HEART)],
    [Card(6, suit.HEART), Card(5, suit.CLUBS), Card(4, suit.HEART), Card(3, suit.SPADE)],
    [None, Card(8, suit.DIAMOND), Card(7, suit.SPADE)],
    [None, None, Card(10, suit.SPADE), Card(9, suit.HEART), Card(8, suit.CLUBS), Card(7, suit.HEART)]
]

cardpile = [Card(2, suit.DIAMOND)]

def rule_move_to_stack(cardFrom, cardTo):
    if cardFrom is None:
        return False
    if cardFrom.number + 1 == cardTo.number and (((cardFrom.suit.value < 3 and cardTo.suit.value > 2) or (cardFrom.suit.value > 2 and cardTo.suit.value < 3)) or (cardTo.suit == None)):
        return True
    return False 

def rule_move_to_fountain(stack, cardFrom, fountain):
    if cardFrom is None:
        return False
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
                for cardIndex, card in enumerate(fromStack):
                    if rule_move_to_stack(card, toStack[len(toStack)-1]):
                        movesAvailable.append(Moves(card, cardIndex, fromStack, toStack, "Fra stack("+str(fromIndex+1)+") " + str(card.suit) + "(" + str(card.number) + ") til stack(" + str(toIndex+1) + ")"))
        for fountain in fountains:
            cardFrom = fromStack[len(fromStack)-1]
            if rule_move_to_fountain(fromStack, cardFrom, fountain):
                movesAvailable.append(Moves(cardFrom, len(fromStack)-1, fromStack, fountain, "Fra stack("+str(fromIndex+1)+") " + str(cardFrom.suit) + "(" + str(cardFrom.number) + ") til fountain " + str(fountain.suit)))
    
    cardpile_topcard = cardpile[len(cardpile)-1]
    for toIndex, toStack in enumerate(stacks):
        if rule_move_to_stack(cardpile_topcard, toStack[len(toStack)-1]):
            movesAvailable.append(Moves(cardpile_topcard, len(cardpile)-1, cardpile, toStack, "Fra cardpile " + str(cardpile_topcard.suit) + "(" + str(cardpile_topcard.number) + ") til stack(" + str(toIndex+1) + ")"))
    for fountain in fountains:
        if rule_move_to_fountain(cardpile, cardpile_topcard, fountain):
            movesAvailable.append(Moves(cardpile_topcard, len(cardpile)-1, cardpile, fountain, "Fra cardpile " + str(cardpile_topcard.suit) + "(" + str(cardpile_topcard.number) + ") til fountain " + str(fountain.suit)))

    return movesAvailable



def _100_points(move):
    #Er det et ACE til fountain er det "bedste" move (Det kan ikke gøre ting værre)
    if move.cardFrom.number == 1 and type(move.toStack) is Fountain:
        return 100
    #Er det et TOER til fountain er det "bedste" move (Det kan ikke gøre ting værre)
    if move.cardFrom.number == 2 and type(move.toStack) is Fountain:
        return 100
    return 0

def _80_points(move):
    #Ryk konge fra anden bunke til tom position for at åbne et NONE felt
    if move.cardFromIndex > 0 and move.fromStack[move.cardFromIndex - 1] == None and move.cardFrom.number == 13 and len(move.toStack) == 0:
        return 80
    return 0

def _75_points(move):
    #Ryk konge fra stack til tom position
    if cardpile[len(cardpile)-1] == move.cardFrom and move.cardFrom.number == 13 and len(move.toStack) == 0:
        return 75
    return 0

def _70_points(move):
    #Ryk kort for at åbne et NONE felt
    if move.cardFromIndex > 0 and move.fromStack[move.cardFromIndex - 1] == None:
        return 70
    return 0

def _50_points(move):
    #Middel point for at rykke et kort til fountain
    if type(move.toStack) is Fountain:
        return 50
    return 0

def _45_points(move):
    #Lidt under middel for at rykke et kort fra cardpile til en stack på bordet
    if cardpile[len(cardpile)-1] == move.cardFrom and type(move.toStack) is list:
        return 45
    return 0

def _35_points(move):
    #Frier en plads så en konge kan rykke der hen (Det specielle her er at det kun er godt hvis der er en konge der kan rykkes til det tomme felt ellers er det rigtig dårligt)
    if move.cardFromIndex == 0 and move.cardFrom.number != 13 and len(move.toStack) > 0:
        return 35
    return 0

def _10_points(move):
    #Alle ting der giver 1 point er næsten ubrugelige (Gør ingen forskel) - Undtagelsen er hvis du skal rykke kort til Fountain og nogle kort blokerer
    if move.cardFromIndex > 0 and move.fromStack[move.cardFromIndex - 1] != None and type(move.toStack) is list:
        return 10
    return 0
def _1_points(move):
    #Absolut ubrugelig. Ryk konge fra tomt felt til anden tomt felt
    if move.cardFromIndex == 0 and move.cardFrom.number == 13 and len(move.toStack) == 0: 
        return 1
    return 0

def get_best_move(movesAvailable):
    bestMove = None
    bestPoint = 0
    point = 0

    for move in movesAvailable:
        point = _100_points(move)
        point = _80_points(move) if point == 0 else point
        point = _75_points(move) if point == 0 else point
        point = _70_points(move) if point == 0 else point
        point = _50_points(move) if point == 0 else point
        point = _45_points(move) if point == 0 else point
        point = _35_points(move) if point == 0 else point
        point = _10_points(move) if point == 0 else point
        point = _1_points(move) if point == 0 else point

        if(point > bestPoint):
            bestMove = move
            bestPoint = point

        if(point == 0): 
            print("Mangler: " + move.description)
        
    return bestMove



originalFountains = copy.deepcopy(fountains)
originalStacks = copy.deepcopy(stacks)
originalCardpile = copy.deepcopy(cardpile)

for x in get_moves():
    print(x.description)

print("best move:")
print(get_best_move(get_moves()).description)