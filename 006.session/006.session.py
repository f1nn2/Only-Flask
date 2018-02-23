from flask import Flask, request, session


app = Flask(__name__)
app.secret_key = 'ooothisissecretkeyooo'

# session => 웹 서버에 저장
#             => 세션 타임 아웃 시간까지 유지
#             => 대부분 웹 서버의 메모리가 허용하는 한도까지 가능


@app.route('/index', methods=['GET', 'POST', 'DELETE'])
def index():
    # delete session
    if request.method == 'DELETE':
        session.pop('username')

        return 'session deleted'

    else:
        # session check
        if 'username' in session:

            return 'Hello {0}'.format(session['username'])
        else:
            # if there is no session
            session['username'] = 'unique value'

            print(session['username'])

            return 'Session appended!'


if __name__ == '__main__':
    app.run(debug=True, port=8080)