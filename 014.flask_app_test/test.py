import unittest
from main import app

# "Something that is untested is broken"
# 위 문구처럼 테스트는 서비스를 개발하는데 있어 빠져서는 안되는 것이다.
# 또한, TDD(테스트 주도 개발) 가 떠오르면서 테스트의 중요성은 더욱 커졌다.
# python 에서 기본으로 제공하는 unittest 로 Flask app 을 테스트 하도록 하였다.


# unittest 의 TestCase 를 상속
class MyFirstTest(unittest.TestCase):
    def setUp(self):
        # Werkzeug 를 통해 테스트 클라이언트를 제공받음
        self.client = app.test_client()

    def tearDown(self):
        print('tearDown')

    def testIndexGET(self):
        # test_client.method 로 원하는 HTTP 요청을 보낼 수 있음
        # query_string 파라미터에 dic 을 전달
        rv = self.client.get('/', query_string={'query_string': 1208})

        # TestCase 클래스에서 제공하는 assert Functions 중 Equals 사용
        self.assertEquals(1208, int(rv.data))

    def testIndexPOST(self):
        # data 파라미타에 dic 을 전달
        # Content-Type 의 기본값이 application/x-www-form-urlencoded 이므로
        # form-data 나 json data 를 보내고 싶으면 헤더를 설정해야 함
        rv = self.client.post('/', data={'body_data': 1208})

        self.assertEquals(1208, int(rv.data))


if __name__ == '__main__':
    unittest.main()
