from flask import Flask,render_template


app = Flask(__name__)


@app.route('/index/<name>')
def index(name):
    # 플라스크는 템플릿 엔진으로 Jinja2 를 내장하고 있음
    # 플라스크가 templates 라는 폴더 안에서 찾기 때문에 패키지 안에 이 폴더가 있어야함
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, port=8080)