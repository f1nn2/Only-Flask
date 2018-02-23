from flask import Flask
from flask_restful import Api, Resource
from flasgger import Swagger, swag_from
# API server 를 개발하면 당연히 API 를 명세한 docs 를 작성해야하는데
# docs 를 작성하는 작업이 여간 귀찮은 것이 아니다. 어떤 변경 사항이 있으면 일일이 문서를 수정해야한다.
# swagger 는 이러한 불편함을 없애기 위해 api docs 를 코드로 자동생성 할 수 있게 해주는 툴이다.
# flasgger 는 flask 를 위한 swagger 패키지 이다.

app = Flask(__name__)

# 수많은 세팅 종류가 있는데, config 와 template 에서 세팅
app.config['SWAGGER'] = {
    'title': 'My New Api',
    'uiversion': 3,

    # swagger UI 정보
    'info': {
        'title': 'simple example api',
        'version': '1.0',
        'description': 'test api'
    },

    'host': 'localhost',
    'basePath': '/api'
}

template = {
    'schemes': [
        'http'
    ],
    
    # 사용할 태그들을 template 에서 미리 정의
    'tags': [
        {
            'name': 'TEST',
            'description': 'flasgger 를 적용한 test api'
        }
    ]
}

swag = Swagger(app, template=template)
api = Api(app)

# docs 를 명세 할 때 한가지 방법만이 있는것이 아니라, docstring, YAML, dict 등의 여러 방법으로 명세할 수 있음
# 여기서는 dict
TEST_API_GET = {
    'tag': ['TEST'],
    'description': '접속한 사용자의 username',
    # 파라미터 명세
    'parameters': [
        {
            'name': 'username',
            'description': 'username',
            'in': 'path',
            'type': 'str',
            'required': True
        }
    ],
    # 요청시 응답 명세
    'response': {
        '200': {
            'description': 'success',
            'example': {
                'application/json': {
                    'username': 'flouie'
                }
            }
        }
    }
}


class Test(Resource):
    # 위에서 정의한 dict 를 데코레이터와 연결
    @swag_from(TEST_API_GET)
    def get(self, username):
        return {'username': username}, 200


api.add_resource(Test, '/test/<username>')


app.run(debug=True)
