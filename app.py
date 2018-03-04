from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/topic')
def topic_list():
	return 'All topics'


@app.route('/topic/<string:name>')
def topic_page(name):
	return 'name info'

	