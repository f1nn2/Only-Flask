from flask import Flask, request


app = Flask(__name__)


@app.route('/test1', methods=['GET', 'POST'])
def test1():
    if request.method == 'GET':
        # query string data, 만약 없다면 400 에러 반환
        qs = request.args['key']

        return 'query string : ' + qs

    elif request.method == 'POST':
        # form data
        form = request.form['test']
        # http header
        print(request.headers)
        # content type 이 json 인지 아닌지
        print(request.is_json)

        return 'form data : ' + form


@app.route('/test2', methods=['GET', 'POST'])
def test2():
    # form data 와 query string 동시에 반환
    print(request.values)

    return 'all data : ' + request.values['form-data']


if __name__ == '__main__':
    app.run(debug=True, port=8080)