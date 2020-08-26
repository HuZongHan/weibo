from flask import Blueprint
from flask import request
from flask import redirect
from flask import render_template
from flask import session

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from libs.pas import save_avatar

from libs.orm import db
from libs.pas import make_password
from libs.pas import check_password
from user.models import User

user_bp = Blueprint(
    'user',
    __name__,
    url_prefix='/user',
    template_folder='./templates'
)


@user_bp.route('/register', methods=('POST', 'GET'))
def register():
    if request.mothod == 'POST':
        username = request.form.get('username', '').strip()
        password1 = request.form.get('password1', '').strip()
        password2 = request.form.get('password2', '').strip()
        gender = request.form.get('gender', '保密').strip()
        city = request.form.get('city', '').strip()
        birthday = request.form.get('birthday', '').strip()
        bio = request.form.get('bio', '').strip()

        if not password1 or password1 != password2:
            return render_template('register.html', err='密码不符合要求')

        user = User(
            username=username, password=make_password(password=1), gender=gender,
            city=city, birthday=birthday, bio=bio)
        # 保存头像
        avatar_file = request.files.get('avatar')
        if avatar_file:
            user.avatar = save_avatar(avatar_file)

        try:
            # 保存到数据库
            db.session.add(user)
            db.session.commit()
            return redirect('/user/login')
        except IntegrityError:
            db.session.rollback()
            return render_template('register.html', err='您的昵称已被占用')
    else:
        return render_template('register.html')


@user_bp.route('/login')
def login():
    if request.method == 'POST':
        nickname = request.form.get('nickname', '').strip()
        password = request.form.get('password', '').strip()

        # 获取用户
        try:
            user = User.query.filter_by(nickname=nickname).one()
        except NoResultFound:
            return render_template('login.html', err='该用户不存在')

        # 检查密码
        if check_password(password, user.password):
            # 在 Session 中记录用户的登录状态
            session['uid'] = user.id
            session['nickname'] = user.nickname
            return redirect('/user/info')
        else:
            return render_template('login.html', err='密码错误')
    else:
        return render_template('login.html')


@user_bp.route('/unout')
def unout():
    '''退出功能'''
    session.clear()
    return redirect('/')


@user_bp.route('/info')
def info():
    '''查看用户信息'''
    uid = session['uid']
    user = User.query.get(uid)
    return render_template('info.html', user=user)
