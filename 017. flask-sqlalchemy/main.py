from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

# ORM(객체 관계 매핑)은 객체와 RDB 를 연결시켜주는 개념이다.
# ORM 을 이용하면 제약을 최대한 적게 받으면서 RDB 를 컨트롤할 수 있다.
# ORM 은 객체지향적으로 모델들을 class 로 작성해서 RDB 와 객체를 연결해보는 것이다.
# 즉, 길고 복잡한 SQL 문을 코드에 쓸 필요 없이 객체지향적으로 프로그래밍할 수 있다.


app = Flask(__name__)
# python 에서 mysql 을 사용하기 위해서는 Python DB API 표준을 따르는 MySQL DB 모듈이 있어야 한다.
# 그 중 pymysql 을 사용했다.
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:germany33@localhost:3305/sample1"

# ORM 중 SQLAlchemy 를 사용한다.
db = SQLAlchemy(app)
from models import *


@app.route('/insert', methods=['POST'])
def insert():
    id = request.form['id']
    pw = request.form['pw']

    # SQL 에서 INSERT INTO 문
    row = User(id=id, pw=pw)
    db.session.add(row)
    db.session.commit()

    return Response('success insert user', 201)


@app.route('/select', methods=['GET'])
def select():
    id = request.args['id']
    # SQL 에서 SELECT 문
    row = User.query.filter_by(id=id).first()

    return jsonify({
        'id': row.id,
        'pw': row.pw,
        'signup_time': row.signup_time
    })


@app.route('/select/all', methods=['GET'])
def select_all():
    # SQL 에서 SELECT * FROM
    row = User.query.filter_by().all()

    return jsonify({
        'users_id': [u.id for u in row],
        'users_pw': [u.pw for u in row]
    })


@app.route('/delete', methods=['DELETE'])
def delete():
    id = request.form['id']

    # SQL 에서 DELETE
    row = User.query.filter_by(id=id).first()
    db.session.delete(row)
    db.session.commit()

    return Response('success delete user', 200)


@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    new_pw = request.form['new_pw']

    # SQL 에서 UPDATE
    row = User.query.filter_by(id=id).first()
    row.pw = new_pw
    db.session.commit()

    return Response('success update pw', 201)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
