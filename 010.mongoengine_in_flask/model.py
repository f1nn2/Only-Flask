from mongoengine import *
# 참고 : http://docs.mongoengine.org/tutorial.html

connect('testDB')

# MongoDB 의 스키마가 없는 것을 사용하여 훨씬 더 좋은 해결책을 제공할 수 있게 되었음
# 일반 ORM 테이블의 구조의 정의와 유사한데, 중요한 차이점은 이 스키마가 MongoDB에 전달되지 않음
# 이 스키마는 애플리케이션 레벨에서만 적용되며, 이로 인해 향후의 변경 사항을 쉽게 관리할 수 있음


# class 가 하나의 collection
# ORM 과 관계형 데이터베이스를 사용하는 것처럼 사용자의 필드와 사용자가 저장할 데이터 유형을 정의해야 함
class User(Document):
    # required = True 란, 필수로 입력되어야 하는 값
    # primary_key 로 설정한 경우, 이것이 식별자가 됨
    username = StringField(required=True, primary_key=True)

    password = StringField(required=True)

    # 디폴트 값 설정 가능, 최대 길이 6
    nickname = StringField(required=True, default='user123', max_length=6)


class Comment(EmbeddedDocument):
    # 댓글은 일반적으로 하나의 게시물과 연결
    # 댓글들을 우편 문서에 직접적으로 포함된 문서들의 목록으로 저장
    # EmbeddedDocument 는 일반적인 Document 와 다르지 않게 취급되어야함, 자체적인 collection 이 없을 뿐
    content = StringField()
    name = StringField(max_length=20)


# Post 를 기본 클래스로 생각할 수 있고, TextPost, ImagePost 및 LinkPost 를 포스트의 하위 클래스로 생각할 수 있음
# 객체 지향적인 상속의 원리와 잘 들어맞음
class Posts(Document):
    title = StringField(max_length=30, required=True)

    # ReferenceField 를 사용하여 게시물 작성자에 대한 참조를 저장
    # ORM 의 외래 키와 유사, 저장할 때 자동으로 참조로 변환되고 로드될 때 참조가 제거됨
    # user 가 삭제되면 그 user 가 쓴 글이 모두 삭제됨
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tag = ListField(StringField(max_length=10))
    comments = ListField(EmbeddedDocumentField(Comment))
    
    # meta 를 True 로 하면 상속 가능
    meta = {'allow_inheritance': True}


class TextPost(Posts):
    content = StringField()


class ImagePost(Posts):
    image_path = StringField()


class LinkPost(Posts):
    link_url = StringField()
