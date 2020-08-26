from libs.orm import db

from weibo.models import Weibo

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
