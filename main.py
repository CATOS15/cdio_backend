from image_processing.img_compare import compare
import cv2
import numpy as np
import ml_solitaire.cut_image
import image_solutions as solution
import algorithm.image_algorithm as alg
import communication_layer.ml_opencv as ml_opencv
import communication_layer.app_alg as app_comm

from flask_cors import CORS
from flask.json import jsonify
from flask import Flask, request
from flask.helpers import make_response
from algorithm.image_algorithm import Fountain, run_algorithm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'back3nd_!cdio'
app.config["IMAGE_UPLOADS"] = "images"
CORS(app)

@app.route('/')
def hello():
    return "CDIO API"

@app.route('/upload', methods=['POST'])
def calculate_solution():    
    imagefile = request.files['file'].read()
    image = cv2.imdecode(np.frombuffer(imagefile, np.uint8), cv2.IMREAD_COLOR)
    
    image_fractions = ml_solitaire.cut_image.cut_img_cut_three(image)

    cv_res = solution.opencv_solution(image_fractions)
    ml_res = solution.ml_solution(image_fractions)

    solitaire_alg = ml_opencv.compare_results(cv_res, ml_res)
    bestmove = alg.run_algorithm(solitaire_alg)
    return app_comm.convert_alg_to_app_json(bestmove)
    
#udelukkende til test af index.html skal ikke ændres!
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

    location = "tableau"
    if move and type(move.toStack) is Fountain:
        location = "fountain"

    res = make_response(jsonify({'message': bestMove["move"].description, "firstcard": firstcard, "secondcard": secondcard, "movemessage": movemessage, 'location': location}), 200)
    return res

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
