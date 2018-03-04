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
    issues_names = [issue for issue, val in data[name].iteritems() if val['allowed']]
    return jsonify(issues_names)


@app.route('/specific/<string:cat>/<string:name>')
def specific_data(cat, name):
    cat = cat.lower()
    name = name.lower()
    return jsonify(data[cat][name]['desc'])


@app.route('/ban/<string:cat>/<string:name>')
def ban(cat, name):
    cat = cat.lower()
    name = name.lower()
    data[cat][name]['allowed'] = False
    return jsonify(True)


@app.route('/unban/<string:cat>/<string:name>')
def unban(cat, name):
    cat = cat.lower()
    name = name.lower()
    data[cat][name]['allowed'] = False
    return jsonify(True)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    print(topic_page('Immigration'))
