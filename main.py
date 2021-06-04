from flask.helpers import make_response
from flask.json import jsonify
from algorithm.image_algorithm import run_algorithm
from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'back3nd_!cdio'
app.config["IMAGE_UPLOADS"] = "C:/Users/Nikolai/Desktop/Python/cdio_backend"
# app.config["IMAGE_TEST"] = url("C:\Users\Nikolai\Desktop\Python\cdio_backend")
CORS(app)

@app.route('/')
def hello():
    return "Test commit"

@app.route('/test', methods = ['POST'])
def test_endpoint():
    print(request.form)
    return "OK", 200

@app.route('/testImage', methods = ['POST'])
def test_endpoint2():
    print(request.data)
    return "OK", 200

@app.route('/upload', methods = ['POST'])
def calculateImage():
    imagefile = request.files.get('file', '')
    imagefile.save("image.jpg")
    print(imagefile.filename)

    dictionary ={   
        "firstcard": "2d",   
        "secondcard": "3c",   
        "movemessage": "move your 2d to your 3c"
    }   

    json_object = json.dumps(dictionary)
    return json_object

@app.route("/algtest", methods = ['POST'])
def algtest():
    description = run_algorithm(request.get_json())
    res = make_response(jsonify({'message': description}), 200)
    return res

if __name__ == '__main__':
    #Vi vil optimalt gerne knytte denne til port 80 
    #men så skal vi have flettet det sammen med nginx 
    #eller gøre så man har permission via service til at bind port 80
    app.run(host='0.0.0.0', port=5005)