from flask import Flask, render_template
from topics.agg import load_data


app = Flask(__name__)
data = load_data()


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home_page():
    return render_template('index.html')


@app.route('/<string:catergory>')
def catergory_list(catergory):
	return list(data.keys())


@app.route('/<string:catergory>/<string:name>')
def topic_page(catergory, name):
    name = name.lower()
    issues_names = list(data[name].keys())
    if len(issues_names) == 1:
        return 'The current issue in {} is {}.'.format(name, issues_names[0])

	    issues = ', '.join(issues_names[:-1]) + ', and ' + issues_names[-1]

    return 'The issues in {} are {}.'.format(name, issues)

# if __name__ == '__main__':
#     print(topic_page('Immigration'))