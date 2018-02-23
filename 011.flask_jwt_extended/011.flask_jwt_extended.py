from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
from datetime import timedelta

# JWT 사용을 위해 flask_jwt_extended 사용, 다른 모듈에 비해 간결하고 이식성이 좋음

# 1. 서버가 요청을 확인 하고 Secret_key 를 통해 Access_token 과 Refresh_token 을 발급함
# 2. 이후 인증이 필요한 요청은 클라이언트가 Authorization Header 에 Access_token 을 담아서 보냄
# 3. 서버는 JWT signature 를 체크하고 Payload 로 부터 정보를 확인
# (access_token 만료시, refresh_token 을 통해 access_token 을 재발급 받음)

app = Flask(__name__)

app.config.update(
    SECRET_KEY='flouieserver123!@#flask2134dm',
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=1),
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=30),
    JWT_HEADER_TYPE='JWT'
)
# access_token 의 만료기간은 짧게하고 refresh_token 의 만료기간은 길게하여 자주 refresh 해주는 것이 좋음

JWTManager(app)
test_id = 'flouie74'
test_pw = '123qwe'


@app.route('/login', methods=['POST'])
def login():
    id = request.form.get('id')
    pw = request.form.get('pw')

    if id == test_id and pw == test_pw:
      return jsonify({
          'access_token': create_access_token(identity=id),
          'refresh_token': create_refresh_token(identity=id)
      }), 200
    else:
        return jsonify({
            'message': 'Incorrect id or pw'
        }), 204


@app.route('/me')
@jwt_required
def me():
    return jsonify({
        'identity':  get_jwt_identity()
    }), 200


@app.route('/refresh')
@jwt_refresh_token_required
def refresh():
    return jsonify({
        'access_token': create_access_token(identity=get_jwt_identity())
    }), 200


if __name__ == '__main__':
    app.run(port=8080)
