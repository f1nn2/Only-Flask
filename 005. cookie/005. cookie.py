from flask import Flask, request, make_response


app = Flask(__name__)

# HTTP는 한번 요청과 응답이 이루어지면 접속이 끊기고 상태정보를 유지하지 않는다 (stateless protocol)
# cookie => 브라우저에 key, value 형식의 텍스트로 저장
#            => 쿠키 생성 시 만료시간을 설정함, 기본값은 브라우저 종료 시점
#            => 한 도메인당 20개까지, 쿠키 하나당 4KB, 총 300개가 가능


@app.route('/index')
def index():
    # 쿠키 정보에 접근
    print(request.cookies.get('username'))
    # 쿠키 값 설정
    res = make_response('give cookie')
    res.set_cookie('username', 'flouie')

    return res


@app.route('/index2')
def index2():
    # cookie 를 지우고 싶을 때는 expires 를 0으로 해준다 (만료)
    res = make_response('del cookie?')
    res.set_cookie('username', ' ', expires=0)

    return res


if __name__ == '__main__':
    app.run(debug=True, port=8080)