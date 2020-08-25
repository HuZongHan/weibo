from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from libs.orm import db
from user.views import user_bp


app = Flask(__name__)
app.secret_key = r'@#$T%DTRDYugwuy7w247dq7*&^t7&^*^*^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://hz:HZHh123!@localhost:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

manager = Manager(app)

db.init_app(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

app.register_blueprint(user_bp)

if __name__ == "__main__":
    manager.run()
