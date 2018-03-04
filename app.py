from flask import Flask
from topics.agg import load_data

app = Flask(__name__)
data = load_data()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/topic')
def topic_list():
	return list(data.keys())


@app.route('/topic/<string:name>')
def topic_page(name):
    name = name.lower()
    issues_names = data[name].keys()
    if len(issues_names) == 1:
        return 'The current issue in {} is {}.'.format(name, issues_names[0])

    issues = ', '.join(issues_names[:-1]) + ', and ' + issues_names[-1]

    return 'The issues in {} are {}.'.format(name, issues)

if __name__ == '__main__':
    print topic_page('Immigration')