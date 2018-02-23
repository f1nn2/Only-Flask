from flask import Flask


# 플라스크 애플리케이션 객체 생성
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask!!'


# 인터프리터에 의해 메인 모듈로 실행되었을 때만 run (만약, 임포트되어 사용되었으면 run 하지 않음)
if __name__ == '__main__':
    # 별도의 인자없이 실행 시 127.0.0.1에서 접근
    # host 인자를 넘겨주면 외부에서도 접근 가능
    # debug 인자를 True 로 하면 디버그 정보를 볼 수 있으며, 변경 내용을 재기동 반영해 준다.
    app.run(debug=True, port=8080)
