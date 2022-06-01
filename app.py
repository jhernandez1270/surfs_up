from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/this_world')
def this_world():
    return 'This is a NEW world'