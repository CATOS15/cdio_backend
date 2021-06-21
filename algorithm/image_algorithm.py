from enum import Enum
import copy
import json
from operator import itemgetter
import image_processing.g_img as g_img
# class suit(Enum):
#     DIAMOND = 1
#     HEART = 2
#     SPADE = 3
#     CLUBS = 4

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

fountains = [
    Fountain(0, g_img.Suits.DIAMOND),
    Fountain(0, g_img.Suits.HEART),
    Fountain(0, g_img.Suits.SPADE),
    Fountain(0, g_img.Suits.CLUB)
]
tableau = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
waste = []



def rule_move_to_tableau(fromCard, toStack):
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
        if(messageformat == "tableau_fountain"):
            moves.append(Move(fromCard, fromCardIndex, fromStack, toStack, "Fra tableau("+str(fromStackIndex+1)+") " + str(fromCard.suit) + "(" + str(fromCard.number) + ") til fountain " + str(fromCard.suit)))
        elif(messageformat == "tableau_tableau"):
            moves.append(Move(fromCard, fromCardIndex, fromStack, toStack, "Fra tableau("+str(fromStackIndex+1)+") " + str(fromCard.suit) + "(" + str(fromCard.number) + ") til tableau(" + str(toStackIndex+1) + ")"))
        elif(messageformat == "waste_tableau"):
            moves.append(Move(fromCard, fromCardIndex, fromStack, toStack, "Fra waste " + str(fromCard.suit) + "(" + str(fromCard.number) + ") til tableau(" + str(toStackIndex+1) + ")"))
        elif(messageformat == "waste_fountain"):
            moves.append(Move(fromCard, fromCardIndex, fromStack, toStack, "Fra waste " + str(fromCard.suit) + "(" + str(fromCard.number) + ") til fountain " + str(fromCard.suit)))

# stackMandatory1 og stackMandatory2 er brugt efter man har foretaget sig et 'move'
# Det er fordi at når man har foretaget sig et 'move' så er de næste 'moves' der skal udregnes kun ud fra de tableau man har benyttet til det første move
def get_moves(stackMandatory1 = None, stackMandatory2 = None): 
    moves = []
    for fromStackIndex, fromStack in enumerate(tableau):
        if len(fromStack) == 0:
            continue
        for toStackIndex, toStack in enumerate(tableau):
            if fromStack != toStack:
                for fromCardIndex, fromCard in enumerate(fromStack):
                    if rule_move_to_tableau(fromCard, toStack):
                        append_legit_move(stackMandatory1, stackMandatory2, fromStack, fromStackIndex, toStack, toStackIndex, moves, fromCard, fromCardIndex, "tableau_tableau")
        for fountainIndex, fountain in enumerate(fountains):
            fromCard = fromStack[len(fromStack)-1]
            if rule_move_to_fountain(fromCard, fountain):
                append_legit_move(stackMandatory1, stackMandatory2, fromStack, fromStackIndex, fountain, fountainIndex, moves, fromCard, fromCardIndex, "tableau_fountain")
    if len(waste) > 0:
        waste_topcard = waste[len(waste)-1]
        for toStackIndex, toStack in enumerate(tableau):
            if rule_move_to_tableau(waste_topcard, toStack):
                append_legit_move(stackMandatory1, stackMandatory2, waste, -1, toStack, toStackIndex, moves, waste_topcard, len(waste)-1, "waste_tableau")
        for fountainIndex, fountain in enumerate(fountains):
            if rule_move_to_fountain(waste_topcard, fountain):
                append_legit_move(stackMandatory1, stackMandatory2, waste, -1, fountain, fountainIndex, moves, waste_topcard, len(waste)-1, "waste_fountain")
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
    #Ryk konge fra waste til tom position
    if len(waste) > 0 and waste[len(waste)-1] == move.fromCard and move.fromCard.number == 13 and len(move.toStack) == 0:
        return 75
    return 0

def _50_points(move):
    #Rykke et kort til fountain
    if type(move.toStack) is Fountain:
        return 50
    return 0

def _45_points(move):
    #Rykke et kort fra waste til en tableau på bordet
    if len(waste) > 0 and waste[len(waste)-1] == move.fromCard and type(move.toStack) is list:
        return 45
    return 0

def _25_points(move):
    #Frier en plads så en konge kan rykke der hen
    alreadyEmtpy = False
    for column in tableau:
        if len(column) == 0:
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

def simulate_newTableau(move):
    global waste, tableau, fountains
    cardMoved = None

    newTableau = [None, None]

    fromIndex = -1

    if move.fromStack == waste:
        cardMoved = waste[move.fromCardIndex:]
        waste = waste[:move.fromCardIndex]
        newTableau[0] = waste
        fromIndex = 999
    else:
        for index, column in enumerate(tableau):
            if(column == move.fromStack):
                cardMoved = column[move.fromCardIndex:]
                tableau[index] = column[:move.fromCardIndex]
                newTableau[0] = tableau[index]
                fromIndex = index
        for index, fountain in enumerate(fountains):
            if(fountain == move.fromStack):
                cardMoved = fountain[move.fromCardIndex:]
                fountains[index] = fountain[:move.fromCardIndex]
                newTableau[0] = fountains[index]
                fromIndex = index

    if fromIndex == -1:
        print("FEJL. Ingen index at rykke kort til??")

    for index, column in enumerate(tableau):
        if(column == move.toStack and cardMoved != None and index != fromIndex):
            tableau[index] = move.toStack + cardMoved
            newTableau[1] = tableau[index]
    for index, fountain in enumerate(fountains):
        if(fountain == move.toStack and index != fromIndex):
            fountains[index].count = fountains[index].count + 1
            newTableau[1] = fountains[index]

    return newTableau

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
    global waste, tableau, fountains
    bestMove = {"point": 0, "move": None, "numberOfMoves": 0}
    moves_ordered1 = get_moves_ordered(get_moves())

    for move in moves_ordered1: 
        newTableau = simulate_newTableau(move["move"])
        moves_ordered2 = get_moves_ordered(get_moves(newTableau[0], newTableau[1]))

        combinedpoint = move["point"]
        if len(moves_ordered2) > 0:
            combinedpoint = move["point"] + moves_ordered2[0]["point"]
        
        if len(moves_ordered2) > 0: #and combinedpoint != 55 and combinedpoint != 60 and combinedpoint != 100:
            if combinedpoint > bestMove["point"]:
                bestMove["point"] = combinedpoint
                bestMove["move"] = move["move"]
                bestMove["numberOfMoves"] = 2
            if combinedpoint == bestMove["point"]:
                if moves_ordered1[0]["point"] > move["point"]:
                    bestMove["point"] = combinedpoint
                    bestMove["move"] = moves_ordered1[0]["move"]
                    bestMove["numberOfMoves"] = 2
        else:
            if move["point"] > bestMove["point"]:
                bestMove["point"] = move["point"]
                bestMove["move"] = move["move"]
                bestMove["numberOfMoves"] = 1

        fountains = copy.copy(originalFountains)
        tableau = copy.copy(originalTableau)
        waste = copy.copy(originalWaste)

    if bestMove["move"] == None:
        return None


    return bestMove


def run_algorithm(data_solitaire):
    global originalFountains, originalTableau, originalWaste, tableau, fountains, waste

    fountains = [
        Fountain(0, g_img.Suits.DIAMOND),
        Fountain(0, g_img.Suits.HEART),
        Fountain(0, g_img.Suits.SPADE),
        Fountain(0, g_img.Suits.CLUB)
    ]
    tableau = [
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    waste = []

    index = 0
    for data_cards in data_solitaire['tableau']:
        for data_card in data_cards:
            if data_card is None:
                tableau[index].append(None)
            else:
                tableau[index].append(Card(data_card['number'], g_img.Suits(data_card['suit'])))
        index += 1

    index = 0
    for data_fountain in data_solitaire['fountains']:
        fountains[index] = Fountain(data_fountain['number'], g_img.Suits(data_fountain['suit']))
        index += 1

    index = 0
    for data_waste in data_solitaire['waste']:
        waste.append(Card(data_waste['number'], g_img.Suits(data_waste['suit'])))
        index += 1

    originalFountains = copy.copy(fountains)
    originalTableau = copy.copy(tableau)
    originalWaste = copy.copy(waste)

    bestMove = set_best_move()

    if fountains[0].count == 13 and fountains[1].count == 13 and fountains[2].count == 13 and fountains[3].count == 13:
        bestMove = {"won": True}
        return bestMove

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
            bestMove["move"].description = "Træk kort! \nHvis ikke muligt udfør -> " + bestMove["move"].description
            bestMove["move"].drawCard = True

    else:
        bestMove = {"move": Move(None,None,None,None,"")}
        bestMove["move"].description = "Træk kort"
        bestMove["move"].drawCard = True
    # print(bestMove)
    return bestMove