from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'back3nd_!cdio'

@app.route('/')
def hello():
    return "Test commit"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
