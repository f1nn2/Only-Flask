from flask import Flask, Response
from flask_mail import Mail, Message

# 웹 서비스의  가장 기본적인 기능중 하나는 사용자에게 이메일을 보내는 기능이다.
# Flask_mail 은 단순한 인터페이스를 제공하여 쉽게 SMTP 를 설정하고 메세지를 보낼 수 있다.
# mail 에 관한 여러가지 설정을 할 수 있으니 공식 문서를 참고하자
# https://pythonhosted.org/Flask-Mail/#configuring-flask-mail

app = Flask(__name__)
app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USERNAME='jerion7474@gmail.com',
    MAIL_PASSWORD='**********',
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
))

# mail 인스턴스 생성
mail = Mail(app)


@app.route('/')
def index():
    # 메일을 보내기위해 가장 먼저 Message 의 인스턴스를 생성한다
    msg = Message("Hello", sender="jerion7474@gmail.com", recipients=["rudtj2316@naver.com"])

    # 메세지에는 body 와 html 태그를 포함시킬 수 있다
    msg.body = "Flask_mail"
    msg.html = "<h2>Flask_mail</h2>"

    # sender 가 2가지 요소를 가질 튜플일 경우, 이름과 주소로 구분된다
    msg2 = Message("Nice to meet you", sender=("Me", "jerion7474@gmail.com"))

    # 수신인의 이메일을 즉시 또는 개별적으로 설정할 수 있다.
    msg2.add_recipient("rudtj2316@naver.com")

    # 마지막으로 메일을 전송할 때는 위에서 만들었던 Mail 인스턴스를 사용한다
    mail.send(msg)
    mail.send(msg2)

    return Response('', 200)


if __name__ == '__main__':
    app.run(port=3030, debug=True)
