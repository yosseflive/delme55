from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
ar=[{"name":"aviel"},{"name":"jacov"}]

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/dt')
def dt():
    return ar


if __name__ == '__main__':
    app.run(debug=True)
