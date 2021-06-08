from flask.helpers import make_response
from flask.json import jsonify
from algorithm.image_algorithm import run_algorithm
from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'back3nd_!cdio'
app.config["IMAGE_UPLOADS"] = "images"
# app.config["IMAGE_TEST"] = url("C:\Users\Nikolai\Desktop\Python\cdio_backend")
CORS(app)

@app.route('/')
def hello():
    return "CDIO API"

@app.route('/upload', methods = ['POST'])
def calculateImage():
    imagefile = request.files.get('file')
    imagefile.save("image.jpg")

    json_object = json.dumps(getAlgData())
    return json_object

@app.route("/algtest")
def algtest():
    json_object = json.dumps(getAlgData())
    return json_object


def getAlgData():
    dictionary = None

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
        firstcard = str(getCardCharFromNumber(move.fromCard.number)) + str(getColourCharFromNumber(move.fromCard.suit))
        secondcard = str(getCardCharFromNumber(move.toCard.number)) + str(getColourCharFromNumber(move.toCard.suit))
        movemessage = str(move.description)

        if (bestMove["point"] < 20 and bestMove["numberOfMoves"] == 1) or (bestMove["point"] < 40 and bestMove["numberOfMoves"] == 2) or len(originalCardpile) == 0:
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

def getColourCharFromNumber(number):
    if number.value == 1:
        return "d"
    if number.value == 2:
        return "h"
    if number.value == 3:
        return "s"
    if number.value == 4:
        return "c"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)