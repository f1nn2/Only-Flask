from werkzeug.security import generate_password_hash as ge_pw_hash
from werkzeug.security import check_password_hash as check_pw_hash

# 패스워드를 그대로 DB 에 저장하는것은 정말 말도 안되는 일이다.
# 당연히 '비밀' 번호 이기에 암호화가 필요한데 단방향 암호화는 해커의 레인보우 테이블 공격에 의해 뚫리고 만다.
# 그래서 'salt' 라는 무작위 문자열을 섞어서 암호화를 하는데
# Werkzeug 에서 해시에 도움을 준다. 덕분에 정말 간단하게 암호화 코드를 작성할 수 있다.


class User(object):
    def __init__(self, id, pw):
        self.id = id
        self.set_password(pw)

    # generate_password_hash 로 password 를 암호화
    def set_password(self, pw):
        self.pw_hash = ge_pw_hash(pw)

    # check_password_hash 로 원래  비밀번호를 확인할 수 있다.
    def check_password(self, pw):
        return check_pw_hash(self.pw_hash, pw)


me = User('Flouie', 'lalalala')
print(me.pw_hash)
print(me.check_password('lalalala'))
print(me.check_password('lalalalall'))
