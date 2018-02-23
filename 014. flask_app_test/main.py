from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return request.form['body_data']

    elif request.method == 'GET':
        return request.args['query_string']


if __name__ == '__main__':
    app.run(debug=True, port=3000)
