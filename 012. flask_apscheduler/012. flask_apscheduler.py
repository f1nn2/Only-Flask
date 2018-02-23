from flask import Flask
from flask_apscheduler import APScheduler
from datetime import datetime

# Python 에는  이미 APScheduler 가 있음
# Flask 를 공부하고 사용하는 입장이므로 Flask 구성에서 스케줄러를 로드할 수 있는 flask_apscheduler 를 알아보았음
# flask_apscheduler 의 feature 는 다음과 같다고 함
"""
    1. Flask 구성에서 스케줄러 구성을 로드
    2. Flask 구성에서 작업 정의를 로드
    3. 스케줄러가 실행할 호스트 이름 지정 가능
    4. 예약된 작업을 관리하는 RESTAPI 를 제공
    5. RESTAPI 에 대한 인증 제공
"""
# docs 도 따로 없고 예제 코드만 있어 개인적으로는 기존 APScheduler 보다 유연하게 사용하기 어려웠음


# 3초마다 현재 시간의 출력하는 함수를 예약
class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'jobs:current_time',
            'args': (datetime.now()),
            'trigger': 'interval',
            'second':  3
        }
    ]

    # SCHEDULER_API_ENABLED = True


def current_time(time):
    print('{0}년 {1}월 {2}일' .format(time.year, time.month, time.day))
    print('{0}시 {1}분 {2}초' .format(time.hour, time.minute, time.second))


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.start()

    app.run()
