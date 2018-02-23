from flask import Flask, g
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)


@app.before_request
def before_first_request():
    def make_logger():
        # RotatingFileHandler
        # => 첫째 인자 : 로그를 남길 파일의 이름
        # => 두번째 인자 : maxBytes 를 채우면 새 로그 파일이 생성
        # => 세번째 인자 : n번째 로그파일이 채워지면 원래 있던 로그파일을 버리고 새 파일 생성
        handler = RotatingFileHandler('server_log.log', maxBytes=15000, backupCount=3)

        # 로그 포매팅
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")

        # 핸들러에 포매터를 달아줌
        handler.setFormatter(formatter)

        # app 객체의 logger 프로퍼티에 핸들러 추가
        app.logger.addHandler(handler)

        # logger 의 레벨 셋팅
        # 설정한 레벨이상에서 로깅됨
        """
            <logger's level>
            CRITICAL = 50
            FATAL = CRITICAL
            ERROR = 40
            WARNING = 30
            WARN = WARNING
            INFO = 20
            DEBUG = 10
            NOTSET = 0
        """
        app.logger.setLevel(logging.INFO)

    make_logger()
    g.logger = app.logger
    print(g.logger)

    g.logger.info('<====Server Logging====>')


@app.route('/index')
def index():
    g.logger.info('Access <index> router')
    return 'logging logging', 200


if __name__ == '__main__':
    app.run(debug=True, port=8080)
