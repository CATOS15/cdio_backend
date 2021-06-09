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

<<<<<<< HEAD
=======
@app.route("/algtest", methods = ['POST'])
def algtestpost():
    bestMove = run_algorithm(request.get_json())
    res = make_response(jsonify({'message': bestMove["move"].description}), 200)
    return res
>>>>>>> 3b66c057f632d5cd93401eea2f663e5176ccdb98

@app.route("/algtest")
def algtestget():
    json_object = json.dumps(run_simulation())
    return json_object

waste = []
noneCards = []
def setupWaste():
    global waste
    for i in range(1, 14):  
        waste.append({'number': i, 'suit': 1})
        waste.append({'number': i, 'suit': 2})
        waste.append({'number': i, 'suit': 3})
        waste.append({'number': i, 'suit': 4})
    random.shuffle(waste)

def setupNoneCards():
    global waste, noneCards
    for i in range(21):  
        noneCards.append(drawCard())

def drawNoneCard():
    global noneCards

    i = 0
    card = noneCards[i]
    del noneCards[i]
    
    return card

def toWaste(card):
    global waste
    waste.append(card)

def drawCard():
    global waste

    i = 0
    card = waste[i]
    del waste[i]
    
    return card

def run_simulation():
    global waste

    firstcard = ""
    secondcard = ""
    movemessage = ""

    setupWaste()
    setupNoneCards()

    data_solitaire = {
        'stacks': [
            [
                drawCard()
            ],
            [
                None,
                drawCard()
            ],
            [
                None,
                None,
                drawCard()
            ],
            [
                None,
                None,
                None,
                drawCard()
            ],
            [
                None,
                None,
                None,
                None,
                drawCard()
            ],
            [
                None,
                None,
                None,
                None,
                None,
                drawCard()
            ],
            [
                None,
                None,
                None,
                None,
                None,
                None,
                drawCard()
            ],
        ],
        'fountains': [
            {'number': 0, 'suit': 1},
            {'number': 0, 'suit': 2},
            {'number': 0, 'suit': 3},
            {'number': 0, 'suit': 4}
        ],
        'cardpile': [
            drawCard()
        ],
    }

    # data_solitaire = {
    #     "stacks":[
    #         [
    #             {
    #                 "number":5,
    #                 "suit":2
    #             },
    #             {
    #                 "number":4,
    #                 "suit":4
    #             }
    #         ],
    #         [
                
    #         ],
    #         [
    #             None,
    #             None,
    #             {
    #                 "number":11,
    #                 "suit":1
    #             },
    #             {
    #                 "number":10,
    #                 "suit":4
    #             },
    #             {
    #                 "number":9,
    #                 "suit":1
    #             },
    #             {
    #                 "number":8,
    #                 "suit":4
    #             },
    #             {
    #                 "number":7,
    #                 "suit":1
    #             },
    #             {
    #                 "number":6,
    #                 "suit":4
    #             },
    #             {
    #                 "number":5,
    #                 "suit":1
    #             }
    #         ],
    #         [
    #             {
    #                 "number":11,
    #                 "suit":4
    #             },
    #             {
    #                 "number":10,
    #                 "suit":1
    #             },
    #             {
    #                 "number":9,
    #                 "suit":3
    #             },
    #             {
    #                 "number":8,
    #                 "suit":2
    #             },
    #             {
    #                 "number":7,
    #                 "suit":3
    #             },
    #             {
    #                 "number":9,
    #                 "suit":3
    #             }
    #         ],
    #         [
    #             None,
    #             {
    #                 "number":4,
    #                 "suit":3
    #             }
    #         ],
    #         [
    #             None,
    #             None,
    #             None,
    #             None,
    #             {
    #                 "number":12,
    #                 "suit":1
    #             },
    #             {
    #                 "number":11,
    #                 "suit":3
    #             }
    #         ],
    #         [
    #             None,
    #             None,
    #             None,
    #             {
    #                 "number":5,
    #                 "suit":3
    #             },
    #             {
    #                 "number":4,
    #                 "suit":2
    #             },
    #             {
    #                 "number":3,
    #                 "suit":3
    #             }
    #         ]
    #     ],
    #     "fountains":[
    #         {
    #             "number":4,
    #             "suit":1
    #         },
    #         {
    #             "number":2,
    #             "suit":2
    #         },
    #         {
    #             "number":0,
    #             "suit":3
    #         },
    #         {
    #             "number":2,
    #             "suit":4
    #         }
    #     ],
    #     "cardpile":[
    #         {
    #             "number":7,
    #             "suit":2
    #         }
    #     ]
    #     }
    print("\n")
    print(data_solitaire)

    for i in range(1, 200):

        for stackIndex, stack in enumerate(data_solitaire['stacks']):
            if len(stack) > 0 and stack[len(stack)-1] is None:
                data_solitaire['stacks'][stackIndex][len(stack)-1] = drawNoneCard()


        bestMove = run_algorithm(data_solitaire)
        #print(str(move.fromCard.number) + str (move.fromCard.suit.value))

        cardsMoved = []

        if data_solitaire['fountains'][0]["number"] == 13 and data_solitaire['fountains'][1]["number"] == 13 and data_solitaire['fountains'][2]["number"] == 13 and data_solitaire['fountains'][3]["number"] == 13:
            return {   
                "firstcard": "new",   
                "secondcard": "new",   
                "movemessage": "Du har vundet!"
            }

        if bestMove["move"].drawCard:
            if len(waste) == 0:
                return {   
                    "firstcard": "new",
                    "secondcard": "new",
                    "movemessage": "Du har tabt!"
                }
            else:
                if data_solitaire['cardpile'][0] is not None:
                    toWaste(data_solitaire['cardpile'][0])
                    data_solitaire['cardpile'][0] = drawCard()
        else:
            if data_solitaire['cardpile'][0]["number"] == bestMove["move"].fromCard.number and data_solitaire['cardpile'][0]["suit"] == bestMove["move"].fromCard.suit.value:
                cardsMoved = data_solitaire['cardpile'].copy()
                if len(waste) != 0:
                    data_solitaire['cardpile'][0] = drawCard()
            else:
                for stackIndex, stack in enumerate(data_solitaire['stacks']):
                    for cardIndex, card in enumerate(stack):
                        if card is not None and card["number"] == bestMove["move"].fromCard.number and card["suit"] == bestMove["move"].fromCard.suit.value:
                            cardsMoved = data_solitaire['stacks'][stackIndex][cardIndex:]
                            data_solitaire['stacks'][stackIndex] = data_solitaire['stacks'][stackIndex][:cardIndex]

            if type(bestMove["move"].toStack) is Fountain:
                data_solitaire['fountains'][bestMove["move"].toCard.suit.value-1]["number"] += 1
            else:
                for stackIndex, stack in enumerate(data_solitaire['stacks']):
                    for cardIndex, card in enumerate(stack):
                        if card is not None:
                            if len(bestMove["move"].toStack) == 0:
                                if len(stack) == 0:
                                    data_solitaire['stacks'][stackIndex] = data_solitaire['stacks'][stackIndex] + cardsMoved
                            elif card["number"] == bestMove["move"].toCard.number and card["suit"] == bestMove["move"].toCard.suit.value:
                                data_solitaire['stacks'][stackIndex] = data_solitaire['stacks'][stackIndex] + cardsMoved
        
        print(data_solitaire['cardpile'][0])
        print(bestMove['move'].description)
        print("\n")


    print("\n")
    print(data_solitaire)
    print("\n")
    print(waste)
    print("\n")
    print(bestMove)

    if bestMove["move"].fromCard is not None and bestMove["move"].toCard is not None:
        firstcard = str(getCardCharFromNumber(bestMove["move"].fromCard.number)) + str(getColourCharFromNumber(bestMove["move"].fromCard.suit))
        secondcard = str(getCardCharFromNumber(bestMove["move"].toCard.number)) + str(getColourCharFromNumber(bestMove["move"].toCard.suit))
        movemessage = str(bestMove["move"].description)

        if (bestMove["point"] < 20 and bestMove["numberOfMoves"] == 1) or (bestMove["point"] < 40 and bestMove["numberOfMoves"] == 2):
            firstcard = "flip"
            secondcard = "random"
    else:
        movemessage = str(bestMove["move"].description)

    return {   
        "firstcard": firstcard,   
        "secondcard": secondcard,   
        "movemessage": movemessage
    }


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
