from flask import Flask


app = Flask(__name__)


# 데코레이터를 통해 라우팅
@app.route('/test')
# view function 을 통해 해당 URI 를 요청했을 때 실행할 기능을 작성
def test():
    return 'Hello Flask!!'


# 동적 URI 라우팅
@app.route('/test1/<name>')
# <변수>를 view function 의 인자로 사용
def test1(name):
    return 'Welcome ' + name


# 동적 변수 타입 변환(정수형 )
@app.route('/test2/<int:num>')
def test2(num):
    return 'q num : %d' % num


# add_url_rule
def test3():
    return 'without decorator'


# rule, endpoint, view function 순서로 인자가 들어간다
app.add_url_rule('/test3', 'end', test3)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
