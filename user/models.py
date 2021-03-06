from libs.orm import db

import random
from libs.pas import random_zh_str


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.Enum('男', '女', '保密'), default='unknown')
    city = db.Column(db.String(10), default='中国')
    avatar = db.Column(db.String(256), default='/static/img/default.png')
    birthday = db.Column(db.Date, default='')
    bio = db.Column(db.Text, default='')
    created = db.Column(db.DateTime, nullable=False)

    @classmethod
    def fake_users(cls, num):
        users = []
        for i in range(num):
            year = random.randint(1980, 2000)
            month = random.randint(1, 12)
            day = random.randint(1, 28)

            nickname = random_zh_str(3)
            password = '1234567890'
            gender = random.choice(['male', 'female', 'unknow'])
            birthday = '%04d-%02d-%02d' % (year, month, day)
            city = random.choice(['上海', '苏州', '长沙', '合肥', '呼和浩特', '青岛', '大理', '铁岭'])
            bio = random_zh_str(30)
            created = '2018-07-19'
            user = cls(nickname=nickname, password=password, gender=gender,
                       birthday=birthday, city=city, bio=bio, created=created)
            users.append(user)
        db.session.add_all(users)
        db.session.commit()
        return users
