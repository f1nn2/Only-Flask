from main import db
from sqlalchemy import Column
from datetime import datetime


# model 을 class 로 
class User(db.Model):
    __tablename__ = 'developers'

    id = Column(db.String(20), nullable=False, primary_key=True, unique=True)
    pw = Column(db.String(40), nullable=False)
    signup_time = Column(db.DateTime, default=datetime.now())


# 모든 model 을 생성
db.create_all()
