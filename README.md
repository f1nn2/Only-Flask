# Flask TIL
- "Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions."
- 파이썬의 대표적인 마이크로 웹 프레임워크 flask TIL(Today I Learned)
- flask 의 대표적 특징
    - WSGI 툴킷인 Werkzueg 에 의존
    - 템플릿 엔진인 JinJa2 에 의존
    - Request Context(라우터의 콜백인자가 아닌 글로벌한 Context 객체에서 관리)
    - 데코레이터를 통한 미들웨어 지원
    - 프레임워크 자체에서 테스트 클라이언트 제공
    - 마이크로 프레임워크의 자유도와 확장성 
- flask [공식 문서](http://flask.pocoo.org/)와 [JoMinGyu](https://github.com/JoMingyu) 님의 github 를 참조했습니다.

<pre>
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name = request.form['name']
    return 'Hello, {}'.format(name), 200


if __name__ == '__main__':
    app.run(port=7401, debug=Ture)

</pre>

