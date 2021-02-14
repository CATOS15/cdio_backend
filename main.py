from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'back3nd_!cdio'

@app.route('/')
def hello():
    return "Test deployment backend"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #Port 80 i stedet? Tror den lige nu er låst af nginx og python skal også køres som en service på et tidspunkt