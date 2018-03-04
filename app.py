from flask import Flask, render_template, jsonify
from topics.agg import load_data


app = Flask(__name__)
data = load_data()


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/awoo')
def awoo_page():
    return render_template('awoo.html')


@app.route('/categories')
def category_list():
    return jsonify(data)

@app.route('/category/<string:name>')
def topic_page(name):
    name = name.lower()
    issues_names = list(data[name].keys())
    return jsonify(data[name])
    # if len(issues_names) == 1:
    #     return 'The current issue in {} is {}.'.format(name, issues_names[0])

    #     issues = ', '.join(issues_names[:-1]) + ', and ' + issues_names[-1]

    # return 'The issues in {} are {}.'.format(name, issues)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    print(topic_page('Immigration'))
