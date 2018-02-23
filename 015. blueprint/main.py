from flask import Flask
from simple_blueprint import simple_blueprint

app = Flask(__name__)
# 블루프린트를 app 객체에 등록할 때는 register_blueprint 메서드로 등록한다
# url_prefix 로 블루프린트가 동작할 url prefix(접두어) 를 정할 수 있다
app.register_blueprint(simple_blueprint, url_prefix='/blueprint')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
