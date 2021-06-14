from flask.helpers import make_response
from flask.json import jsonify
from algorithm.image_algorithm import Fountain, run_algorithm
from flask import Flask, request
from flask_cors import CORS
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'back3nd_!cdio'
app.config["IMAGE_UPLOADS"] = "images"
# app.config["IMAGE_TEST"] = url("C:\Users\Nikolai\Desktop\Python\cdio_backend")
CORS(app)


@app.route('/')
def hello():
    return "CDIO API"

@app.route('/upload', methods=['POST'])
def calculateImage():
    imagefile = request.files.get('file')
    imagefile.save("image.jpg")

    json_object = json.dumps(getAlgData())
    return json_object

@app.route("/algtest", methods = ['POST'])
def algtestpost():
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

    location = "stack"
    if move and type(move.toStack) is Fountain:
        location = "fountain"

    res = make_response(jsonify({'message': bestMove["move"].description, "firstcard": firstcard, "secondcard": secondcard, "movemessage": movemessage, 'location': location}), 200)
    return res

def getAlgData():
    data_solitaire = {
        'stacks': [
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
        'cardpile': [
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
