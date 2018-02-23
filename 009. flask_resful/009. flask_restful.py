from flask import Flask, request
from flask_restful import Api, Resource
# flask_restful 모듈을 이용하여 쉽게 REST API 를 구현 가능

app = Flask(__name__)
# api 객체를 얻어냄
api = Api(app)


# flask_restful 의 Resource 클래스를 상속 받은 클래스는 uri 에 대한 자원이 됨
class TempLogin(Resource):
    # 라우터가 기존 데코레이터 방식과 달리 메소드화
    # 쓰고자 하는 HTTP method 의 이름으로 메서드를 만들면 됨
    def post(self):
        # 간단한 임시 로그인 예제
        new_username = request.form['username']
        new_pw = request.form['pw']
        if new_username == 'flouie74' and new_pw == 'qwer1234':
            return 'login success', 200
        else:
            return 204


# 만든 리소스와 uri 를 매핑
api.add_resource(TempLogin, '/auth')


if __name__ == '__main__':
    app.run(debug=True, port=8080)