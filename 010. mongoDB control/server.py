from flask import Flask
from model import *

app = Flask(__name__)

# <<Create of CRUD>>
ross = User(username='flouie74', password='qwer1234', nickname='flo')
ross.save()

# <<Read of CRUD>>
# ClassName.objects 로 데이터를 가져올 수 있음
# 반환값은 queryset, list 캐스팅이 가능
for user in User.objects(password='qwer1234'):
    print(user.username)


u = User.objects()

# list 캐스팅
print(list(u))

# 즉시 데이터를 반환할 필요가 있을 경우, as_pymongo() 를 사용
print(list(u.as_pymongo()))

# as_pymongo 는 value 가 None 인 key 제거함 그래서 직접 데이터를 가져와서 dic 을 만드는 것이 좋음
print(u.first())
print(u.first().username)

# 카운팅
print(User.objects.count())

# <<Update of CRUD>>
print('Before : ' + User.objects(username='flouie74').first().nickname)
User.objects(username='flouie74').first().update(nickname='server')
print('After : ' + User.objects(username='flouie74').first().nickname)

# <<Delete of CRUD>>
User.objects().delete()

if __name__ == '__main__':
    app.run(debug=True, port=8080)