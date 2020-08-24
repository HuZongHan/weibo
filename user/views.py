from flask import Blueprint
# from user.models import User
from flask import render_template

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_bp.template_folder = './templates'


@user_bp.route('/register')
def register():
    return render_template('register.html')


@user_bp.route('/login')
def login():
    # User.query.get(123)
    return render_template('login.html')


@user_bp.route('/info')
def info():
    return render_template('info.html')

@user_bp.route('/unout')
def unout():
    return render_template('register.html')
