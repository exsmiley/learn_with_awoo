from flask import Flask, render_template, jsonify
from topics.agg import load_data


app = Flask(__name__)
data = load_data()
log = ['Heard about science: space exploration!', 'Heard about immigration: citizenship test!']


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/portal')
def portal_page():
    return render_template('portal.html')

@app.route('/parentportal')
def parentportal_page():
    return render_template('parentportal.html')    


@app.route('/awoo')
def awoo_page():
    return render_template('awoo.html')


@app.route('/categories')
def category_list():
    return jsonify(list(data.keys()))

@app.route('/category/<string:name>')
def topic_page(name):
    name = name.lower()
    issues_names = [issue for issue, val in data[name].iteritems() if val['allowed']]
    return jsonify(issues_names)


@app.route('/specific/<string:cat>/<string:name>')
def specific_data(cat, name):
    cat = cat.lower()
    name = name.lower()
    log.append('Heard about {}: {}!'.format(cat, name))
    data[cat][name]['visited'] = True
    # TODO maybe add restriction
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

@app.route('/all_data')
def all_data():
    return jsonify({'data': data, 'log': log[::-1]})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    print(topic_page('Immigration'))
