from flask import Flask, request
import werkzeug


app = Flask(__name__)
app.config['SECRET_KEY'] = 'back3nd_!cdio'
app.config["IMAGE_UPLOADS"] = "C:/Users/Nikolai/Desktop/Python/cdio_backend"
# app.config["IMAGE_TEST"] = url("C:\Users\Nikolai\Desktop\Python\cdio_backend")

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
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    imagefile.save(filename)
    print(imagefile.filename)
    return "OK", 200

if __name__ == '__main__':
    #Vi vil optimalt gerne knytte denne til port 80 
    #men så skal vi have flettet det sammen med nginx 
    #eller gøre så man har permission via service til at bind port 80
    app.run(host='0.0.0.0', port=5005) 