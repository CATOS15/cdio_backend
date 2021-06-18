from flask.json import jsonify
from flask.helpers import make_response
from algorithm.image_algorithm import Fountain, run_algorithm
from flask import request

def simple_test():
    bestMove = run_algorithm(request.get_json())
    if "won" in bestMove and bestMove["won"]:
        res = make_response(jsonify({'message': "VANDT!", "firstcard": "won", "secondcard": "won", "movemessage": "", 'location': ""}), 200)
        return res

    move = bestMove["move"]

    firstcard = ""
    secondcard = ""
    movemessage = ""

    if type(move) != str and move.fromCard is not None:
        firstcard = str(getCardCharFromNumberTest(move.fromCard.number)) + " " + str(getColourCharFromNumberTest(move.fromCard.suit))
        if move.toCard is not None:
            secondcard = str(getCardCharFromNumberTest(move.toCard.number)) + " " + str(getColourCharFromNumberTest(move.toCard.suit))
        else:
            secondcard = "empty"
        movemessage = str(move.description)

        if (bestMove["point"] < 20 and bestMove["numberOfMoves"] == 1) or (bestMove["point"] < 40 and bestMove["numberOfMoves"] == 2):
            firstcard = "flip"
            secondcard = "random"
    else:
        movemessage = str(move)

    location = "tableau"
    if move and type(move.toStack) is Fountain:
        location = "fountain"

    res = make_response(jsonify({'message': bestMove["move"].description, "firstcard": firstcard, "secondcard": secondcard, "movemessage": movemessage, 'location': location}), 200)

def getAlgData():
    data_solitaire = {
        'tableau': [
            [
                {'number': 8, 'suit': 3}
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
        'waste': [
            {'number': 8, 'suit': 2}
        ],
    }

    bestMove = run_algorithm(data_solitaire)
    move = bestMove["move"]

    firstcard = ""
    secondcard = ""
    movemessage = ""

    if type(move) != str:
        firstcard = str(getCardCharFromNumber(move.fromCard.number)) + \
            str(getColourCharFromNumber(move.fromCard.suit))
        secondcard = str(getCardCharFromNumber(move.toCard.number)) + \
            str(getColourCharFromNumber(move.toCard.suit))
        movemessage = str(move.description)

        if (bestMove["point"] < 20 and bestMove["numberOfMoves"] == 1) or (bestMove["point"] < 40 and bestMove["numberOfMoves"] == 2):
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
