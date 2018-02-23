from flask import Flask, make_response, jsonify, send_from_directory


app = Flask(__name__)


@app.route('/index')
def index():
    # view function 의 리턴값으로 문자열을 주면 자동으로 'text/html' 로 반환
    # view function 의 기본적인 리턴값은 (response, status, header)
    return 'test2017'


@app.route('/index2')
def index2():
    # 응답 객체를 수정해야하거나 헤더를 추가해야 할 때 make_response 사용
    res = make_response('data', 200)
    res.headers['testHeader'] = 'val'
    return res


@app.route('/index3')
def index3():
    res = [{'name': 'JKS', 'age': 17}, {'name': 'JYJ', 'age': 18}]
    # 위에서 리스트는  json array 에, 딕셔너리는 json object 에 대응된다
    # jsonify 를 사용하면 content-type 이 json 으로 자동 변환되며 문자열로 반환한다.
    return jsonify(res)


@app.route('/index4')
def index4():
    # send_from_directory 를 사용하여 간단하게 file response 
    return send_from_directory('./', 'testFile.txt')


if __name__ == '__main__':
    app.run(debug=True, port=8080)