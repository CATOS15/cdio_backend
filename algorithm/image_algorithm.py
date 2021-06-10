from enum import Enum
import copy
import json
from operator import itemgetter
class suit(Enum):
    DIAMOND = 1
    HEART = 2
    SPADE = 3
    CLUBS = 4

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    def toJSON (self):
        return json.dumps(self.__dict__)

class Fountain:
    def __init__(self, count, suit):
        self.count = count
        self.suit = suit
    def toJSON (self):
        return json.dumps(self.__dict__)

class Move:
    def __init__(self, fromCard, fromCardIndex, fromStack, toStack, description):
        self.fromCard = fromCard
        self.fromCardIndex = fromCardIndex
        self.fromStack = fromStack
        self.toStack = toStack
        self.description = description
    def toJSON (self):
        return json.dumps(self.__dict__)

#Ledig plads for en konge bliver Card(14, None)

# fountains = [
#     Fountain(1, suit.DIAMOND),
#     Fountain(1, suit.HEART),
#     Fountain(2, suit.SPADE),
#     Fountain(0, suit.CLUBS)
# ] 

# stacks = [
#     [Card(13, suit.SPADE), Card(12, suit.DIAMOND), Card(11, suit.CLUBS), Card(10, suit.DIAMOND), Card(9, suit.CLUBS)],
#     [Card(13, suit.CLUBS)],
#     [Card(11, suit.HEART)],
#     [],
#     [Card(6, suit.HEART), Card(5, suit.CLUBS), Card(4, suit.HEART), Card(3, suit.SPADE)],
#     [None, Card(8, suit.DIAMOND), Card(7, suit.SPADE)],
#     [None, None, Card(10, suit.SPADE), Card(9, suit.HEART), Card(8, suit.CLUBS), Card(7, suit.HEART)]
# ]

#cardpile = [Card(7, suit.DIAMOND)]

fountains = [
    Fountain(0, suit.DIAMOND),
    Fountain(0, suit.HEART),
    Fountain(0, suit.SPADE),
    Fountain(0, suit.CLUBS)
]
stacks = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
cardpile = []



def rule_move_to_stack(fromCard, toStack):
    if len(toStack) == 0:
        if fromCard is not None and fromCard.number == 13:
            return True
        return False
    toCard = toStack[len(toStack)-1]
    if fromCard is None or toCard is None: #Hvis det er et facedown kort så skal den ikke med.
        return False
    if fromCard.number + 1 == toCard.number and ((fromCard.suit.value < 3 and toCard.suit.value > 2) or (fromCard.suit.value > 2 and toCard.suit.value < 3)):
        return True
    return False 

def rule_move_to_fountain(fromCard, fountain):
    if fromCard is not None and fromCard.number == fountain.count + 1 and fromCard.suit == fountain.suit:
        return True
    return False

def append_legit_move(stackMandatory1, stackMandatory2, fromStack, fromStackIndex, toStack, toStackIndex, moves, fromCard, fromCardIndex, messageformat):
    if stackMandatory1 == None or stackMandatory2 == None or fromStack == stackMandatory1 or fromStack == stackMandatory2 or toStack == stackMandatory1 or toStack == stackMandatory2:
        if(messageformat == "stack_fountain"):
            moves.append(Move(fromCard, fromCardIndex, fromStack, toStack, "Fra stack("+str(fromStackIndex+1)+") " + str(fromCard.suit) + "(" + str(fromCard.number) + ") til fountain " + str(fromCard.suit)))
        elif(messageformat == "stack_stack"):
            moves.append(Move(fromCard, fromCardIndex, fromStack, toStack, "Fra stack("+str(fromStackIndex+1)+") " + str(fromCard.suit) + "(" + str(fromCard.number) + ") til stack(" + str(toStackIndex+1) + ")"))
        elif(messageformat == "cardpile_stack"):
            moves.append(Move(fromCard, fromCardIndex, fromStack, toStack, "Fra cardpile " + str(fromCard.suit) + "(" + str(fromCard.number) + ") til stack(" + str(toStackIndex+1) + ")"))
        elif(messageformat == "cardpile_fountain"):
            moves.append(Move(fromCard, fromCardIndex, fromStack, toStack, "Fra cardpile " + str(fromCard.suit) + "(" + str(fromCard.number) + ") til fountain " + str(fromCard.suit)))

# stackMandatory1 og stackMandatory2 er brugt efter man har foretaget sig et 'move'
# Det er fordi at når man har foretaget sig et 'move' så er de næste 'moves' der skal udregnes kun ud fra de stacks man har benyttet til det første move
def get_moves(stackMandatory1 = None, stackMandatory2 = None): 
    moves = []
    for fromStackIndex, fromStack in enumerate(stacks):
        if len(fromStack) == 0:
            continue
        for toStackIndex, toStack in enumerate(stacks):
            if fromStack != toStack:
                for fromCardIndex, fromCard in enumerate(fromStack):
                    if rule_move_to_stack(fromCard, toStack):
                        append_legit_move(stackMandatory1, stackMandatory2, fromStack, fromStackIndex, toStack, toStackIndex, moves, fromCard, fromCardIndex, "stack_stack")
        for fountainIndex, fountain in enumerate(fountains):
            fromCard = fromStack[len(fromStack)-1]
            if rule_move_to_fountain(fromCard, fountain):
                append_legit_move(stackMandatory1, stackMandatory2, fromStack, fromStackIndex, fountain, fountainIndex, moves, fromCard, fromCardIndex, "stack_fountain")
    if len(cardpile) > 0:
        cardpile_topcard = cardpile[len(cardpile)-1]
        for toStackIndex, toStack in enumerate(stacks):
            if rule_move_to_stack(cardpile_topcard, toStack):
                append_legit_move(stackMandatory1, stackMandatory2, cardpile, -1, toStack, toStackIndex, moves, cardpile_topcard, len(cardpile)-1, "cardpile_stack")
        for fountainIndex, fountain in enumerate(fountains):
            if rule_move_to_fountain(cardpile_topcard, fountain):
                append_legit_move(stackMandatory1, stackMandatory2, cardpile, -1, fountain, fountainIndex, moves, cardpile_topcard, len(cardpile)-1, "cardpile_fountain")
    return moves

def _100_points(move):
    #Er det et ACE til fountain er det "bedste" move (Det kan ikke gøre ting værre)
    if move.fromCard.number == 1 and type(move.toStack) is Fountain:
        return 100
    #Er det et TOER til fountain er det "bedste" move (Det kan ikke gøre ting værre)
    if move.fromCard.number == 2 and type(move.toStack) is Fountain:
        return 100
    return 0

def _95_points(move):
    #Ryk konge fra anden bunke til tom position for at åbne et NONE felt
    if move.fromCardIndex > 0 and move.fromStack[move.fromCardIndex - 1] == None and move.fromCard.number == 13 and len(move.toStack) == 0:
        return 95
    return 0

def _90_points(move):
    #Ryk kort for at åbne et NONE felt
    if move.fromCardIndex > 0 and move.fromStack[move.fromCardIndex - 1] == None:
        return 90
    return 0

def _70_points(move):
    #Ryk konge fra cardpile til tom position
    if len(cardpile) > 0 and cardpile[len(cardpile)-1] == move.fromCard and move.fromCard.number == 13 and len(move.toStack) == 0:
        return 75
    return 0

def _50_points(move):
    #Rykke et kort til fountain
    if type(move.toStack) is Fountain:
        return 50
    return 0

def _45_points(move):
    #Rykke et kort fra cardpile til en stack på bordet
    if len(cardpile) > 0 and cardpile[len(cardpile)-1] == move.fromCard and type(move.toStack) is list:
        return 45
    return 0

def _25_points(move):
    #Frier en plads så en konge kan rykke der hen
    alreadyEmtpy = False
    for stack in stacks:
        if len(stack) == 0:
            alreadyEmtpy = True
            break
    if move.fromCardIndex == 0 and move.fromCard.number != 13 and len(move.toStack) > 0 and not alreadyEmtpy:
        return 25
    return 0
    
def _10_points(move):
    #Alle ting der giver 10 point er næsten ubrugelige (Gør ingen forskel) - Undtagelsen er hvis du skal rykke kort til Fountain og nogle kort blokerer
    if move.fromCardIndex > 0 and move.fromStack[move.fromCardIndex - 1] != None and type(move.toStack) is list:
        return 10
    return 0

# def _2_points(move):
#     #Frier en plads så en konge kan rykke der hen (Dårligt da denne kun bliver ramt hvis der allerede er en tom plads)
#     if move.fromCardIndex == 0 and move.fromCard.number != 13 and len(move.toStack) > 0:
#         return 2
#     return 0
    
# def _1_points(move):
#     #Absolut ubrugelig. Ryk konge fra tomt felt til anden tomt felt
#     if move.fromCardIndex == 0 and move.fromCard.number == 13 and len(move.toStack) == 0: 
#         return 1
#     return 0

def simulate_newStacks(move):
    global cardpile, stacks, fountains
    cardMoved = None

    newStacks = [None, None]

    fromIndex = -1

    if move.fromStack == cardpile:
        cardMoved = cardpile[move.fromCardIndex:]
        cardpile = cardpile[:move.fromCardIndex]
        newStacks[0] = cardpile
        fromIndex = 999
    else:
        for index, stack in enumerate(stacks):
            if(stack == move.fromStack):
                cardMoved = stack[move.fromCardIndex:]
                stacks[index] = stack[:move.fromCardIndex]
                newStacks[0] = stacks[index]
                fromIndex = index
        for index, fountain in enumerate(fountains):
            if(fountain == move.fromStack):
                cardMoved = fountain[move.fromCardIndex:]
                fountains[index] = fountain[:move.fromCardIndex]
                newStacks[0] = fountains[index]
                fromIndex = index

    if fromIndex == -1:
        print("FEJL. Ingen index at rykke kort til??")

    for index, stack in enumerate(stacks):
        if(stack == move.toStack and cardMoved != None and index != fromIndex):
            stacks[index] = move.toStack + cardMoved
            newStacks[1] = stacks[index]
    for index, fountain in enumerate(fountains):
        if(fountain == move.toStack and index != fromIndex):
            fountains[index].count = fountains[index].count + 1
            newStacks[1] = fountains[index]

    return newStacks

def get_moves_ordered(moves):
    moves_ordered = []

    for move in moves:
        point = _100_points(move)
        point = _95_points(move) if point == 0 else point
        point = _90_points(move) if point == 0 else point
        point = _70_points(move) if point == 0 else point
        point = _50_points(move) if point == 0 else point
        point = _45_points(move) if point == 0 else point
        point = _25_points(move) if point == 0 else point
        point = _10_points(move) if point == 0 else point
        # point = _2_points(move) if point == 0 else point
        # point = _1_points(move) if point == 0 else point

        if point > 0:
            moves_ordered.append({"point": point, "move": move})
        # else:
        #     print("FEJL! Et træk har 0 point: " + move.description)
    
    moves_ordered = sorted(moves_ordered, key=itemgetter('point'), reverse=True)
    #print(moves_ordered)
    return moves_ordered

def set_best_move():
    global cardpile, stacks, fountains
    bestMove = {"point": 0, "move": None, "numberOfMoves": 0}
    moves_ordered1 = get_moves_ordered(get_moves())

    for move in moves_ordered1: 
        newStacks = simulate_newStacks(move["move"])
        moves_ordered2 = get_moves_ordered(get_moves(newStacks[0], newStacks[1]))

        combinedpoint = move["point"]
        if len(moves_ordered2) > 0:
            combinedpoint = move["point"] + moves_ordered2[0]["point"]
        
        if len(moves_ordered2) > 0 and combinedpoint != 55 and combinedpoint != 100:
            if combinedpoint > bestMove["point"]:
                bestMove["point"] = combinedpoint
                bestMove["move"] = move["move"]
                bestMove["numberOfMoves"] = 2
        else:
            if move["point"] > bestMove["point"]:
                bestMove["point"] = move["point"]
                bestMove["move"] = move["move"]
                bestMove["numberOfMoves"] = 1

        fountains = copy.copy(originalFountains)
        stacks = copy.copy(originalStacks)
        cardpile = copy.copy(originalCardpile)

    if bestMove["move"] == None:
        return None


    return bestMove


def run_algorithm(data_solitaire):
    global originalFountains, originalStacks, originalCardpile, stacks, fountains, cardpile

    fountains = [
        Fountain(0, suit.DIAMOND),
        Fountain(0, suit.HEART),
        Fountain(0, suit.SPADE),
        Fountain(0, suit.CLUBS)
    ]
    stacks = [
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    cardpile = []

    index = 0
    for data_cards in data_solitaire['stacks']:
        for data_card in data_cards:
            if data_card is None:
                stacks[index].append(None)
            else:
                stacks[index].append(Card(data_card['number'], suit(data_card['suit'])))
        index += 1

    index = 0
    for data_fountain in data_solitaire['fountains']:
        fountains[index] = Fountain(data_fountain['number'], suit(data_fountain['suit']))
        index += 1

    index = 0
    for data_cardpile in data_solitaire['cardpile']:
        cardpile.append(Card(data_cardpile['number'], suit(data_cardpile['suit'])))
        index += 1

    originalFountains = copy.copy(fountains)
    originalStacks = copy.copy(stacks)
    originalCardpile = copy.copy(cardpile)

    bestMove = set_best_move()

    #for x in get_moves():
        #print(x.description)

    #print("\n")
    #print("Bedste træk:")
    #if bestMove != None:
        #print("Antal træk " + str(bestMove["numberOfMoves"]) + " giver " + str(bestMove["point"]) + " point")
        #print(bestMove["move"].description)

    if(bestMove != None):
        bestMove["move"].drawCard = False
        if type(bestMove["move"].toStack) is Fountain:
            bestMove["move"].toCard = Card(bestMove["move"].toStack.count, bestMove["move"].toStack.suit)
        else:
            if len(bestMove["move"].toStack) > 0:
                toCard = bestMove["move"].toStack[len(bestMove["move"].toStack)-1]
                if toCard is None:
                    print("Fejl da kortet er None")
                bestMove["move"].toCard = Card(toCard.number, toCard.suit)
            else:
                bestMove["move"].toCard = None

        if (bestMove["point"] < 20 and bestMove["numberOfMoves"] == 1) or (bestMove["point"] < 40 and bestMove["numberOfMoves"] == 2):
            bestMove["move"].description = "Træk kort! Hvis ikke muligt udfør -> " + bestMove["move"].description
            bestMove["move"].drawCard = True

    else:
        bestMove = {"move": Move(None,None,None,None,"")}
        bestMove["move"].description = "Træk kort"
        bestMove["move"].drawCard = True
        
    return bestMove