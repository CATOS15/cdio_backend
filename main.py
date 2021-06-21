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
    
@app.route("/algtest", methods = ['POST'])
def algtestpost():
    res = alg.simple_test()
    return res



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
