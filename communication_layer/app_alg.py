def convert_alg_to_app_json(bestmove):
    # result = {}
    move = bestmove["move"]
    if move == None or move.fromCard == None or move.toCard == None:
        return {
            "firstcard": "No card",
            "secondcard": "No card",
            "movemessage": "failure"
        }
    # if move.fromCard.number == None :            
    #     result["firstcard"] = "cannot identify first card"

    # if move.toCard.number == None:
    #     result["secondcard"] = "cannot identify second card"

    if type(move) != str:
        firstcard = str(getCardCharFromNumber(move.fromCard.number)) + \
            str(getColourCharFromNumber(move.fromCard.suit))
        secondcard = str(getCardCharFromNumber(move.toCard.number)) + \
            str(getColourCharFromNumber(move.toCard.suit))
        movemessage = str(move.description)

        if (bestmove["point"] < 20 and bestmove["numberOfMoves"] == 1) or (bestmove["point"] < 40 and bestmove["numberOfMoves"] == 2):
            firstcard = "flip"
            secondcard = "random"
    else:
        movemessage = str(move)

    return {
        "firstcard": firstcard,
        "secondcard": secondcard,
        "movemessage": movemessage
    }



def getCardCharFromNumber(number):
    if number == 1:
        return "a"
    if number == 11:
        return "j"
    if number == 12:
        return "q"
    if number == 13:
        return "k"
    return number

def getCardCharFromNumberTest(number):
    if number == 1:
        return "A"
    if number == 11:
        return "J"
    if number == 12:
        return "Q"
    if number == 13:
        return "K"
    return number

def getColourCharFromNumber(number):
    if number.value == 1:
        return "d"
    if number.value == 2:
        return "h"
    if number.value == 3:
        return "s"
    if number.value == 4:
        return "c"


def getColourCharFromNumberTest(number):
    if number.value == 1:
        return "diamond"
    if number.value == 2:
        return "heart"
    if number.value == 3:
        return "spade"
    if number.value == 4:
        return "club"
