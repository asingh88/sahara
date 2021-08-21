import random
from flask import Flask, abort, Response
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)
