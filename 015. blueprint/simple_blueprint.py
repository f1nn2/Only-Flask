from flask import Blueprint

# 플라스크 공식문서에 따르면 플라스크는 어플리케이션을 블루프린트의 집합으로 고려하는데 이 방식은 대형 어플리케이션에 있어서 이상적라고 한다
# 어플리케이션 객체를 인스턴스화하고, 블루프린트의 묶음을 등록할 수 있다.

# 플라스크 블루프린트는 다음과 같은 것들을 제공한다.
# 1. 블루프린트별 URL Rule 설정(접두어, 서브도메인)
# 2. 블루프린트별 URL 핸들러 설정(@before_request 등)
# 3. 블루프린트별 정적 파일 및 템플릿 등을 설정

simple_blueprint = Blueprint('simple_blueprint', __name__)


@simple_blueprint.route('/')
def index():
    return 'blueprint!'
