from flask.helpers import make_response
from flask.json import jsonify
from algorithm.image_algorithm import Fountain, run_algorithm
from flask import Flask, request
from flask_cors import CORS

import ml_solitaire.cut_image

import cv2
import json

import image_solutions as solution
import communication_layer.ml_alg as comm
import algorithm.image_algorithm as alg

import numpy as np

import tests.algorithm.test_endpoint as alg

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
    image = cv2.imdecode(np.fromstring(imagefile, np.uint8), cv2.IMREAD_COLOR)
    
    three_image_tuple = ml_solitaire.cut_image.cut_img_cut_three(image)

    cv_results = solution.opencv_solution(three_image_tuple)
    ml_results = solution.ml_solution(three_image_tuple)

    solitaire_alg = {}
    solitaire_alg['waste'] = comm.map_opencv_alg(cv_results[0], comm.ImageCardType.Waste)
    solitaire_alg['fountains'] = comm.map_opencv_alg(cv_results[1], comm.ImageCardType.Foundation)
    solitaire_alg['tableau'] = comm.map_opencv_alg(ml_results[2], comm.ImageCardType.Tableau)
    bestmove = alg.run_algorithm(solitaire_alg)
    return json.dumps(bestmove["move"].description)

@app.route("/algtest", methods = ['POST'])
def algtestpost():
    res = alg.simple_test()
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
