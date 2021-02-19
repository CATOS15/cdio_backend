from flask import Flask, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'back3nd_!cdio'

@app.route('/')
def hello():
    return "Test commit"

@app.route('/upload', methods = ['POST'])
def calculateImage():
    imagefile = request.files.get('image', '')
    print(imagefile.filename)
    return "OK", 200

if __name__ == '__main__':
    #Vi vil optimalt gerne knytte denne til port 80 
    #men så skal vi have flettet det sammen med nginx 
    #eller gøre så man har permission via service til at bind port 80
    app.run(host='0.0.0.0', port=5005) 