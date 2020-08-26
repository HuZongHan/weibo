from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from libs.orm import db
from user.views import user_bp
from weibo.views import weibo_bp
from weibo.models import Weibo
from flask import redirect
from user.models import User

app = Flask(__name__)
app.secret_key = r'@#$T%DTRDYugwuy7w247dq7*&^t7&^*^*^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hz:HZHh123!@localhost:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

manager = Manager(app)

db.init_app(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

app.register_blueprint(user_bp)
app.register_blueprint(weibo_bp)


@app.route('/')
def home():
    '''首页'''
    return redirect('/weibo/index')


@manager.command
def create_test_weibo():
    '''创建微博测试数据'''
    users = User.fake_users(50)
    uid_list = [u.id for u in users]
    Weibo.fake_weibos(uid_list, 5000)


if __name__ == "__main__":
    manager.run()
