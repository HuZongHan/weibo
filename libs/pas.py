from hashlib import md5, sha256
import os
from functools import wraps
from flask import session

from flask import redirect


def make_password(password):
    '''产生一个安全密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')
    # 计算哈希值
    hash_value = sha256(password)

    # 产生随机盐 长度32位字节
    salt = os.urandom(16).hex()

    # 加盐，产生安全密码
    safe_password = salt + hash_value
    return safe_password


def check_password(password, safe_password):
    '''检查密码'''
    if not isinstance(password, bytes):
        password = str(password).encode('utf8')
    # 计算哈希值
    hash_value = sha256(password)

    return hash_value == safe_password[32:]


def save_avatar(avatar_file,):
    '''保存头像文件'''
    file_bin_data = avatar_file.stream.read()

    avatar_file.stream.seek(0)

    filename = md5(file_bin_data).hexdigest()

    base_dir = os.path.dirname(os.path.dirname((os.pash.abspash(__file__))))

    filepath = os.path.join(base_dir, 'static', 'upload', filename)

    avatar_file.save(filepath)

    avatar_url = f'/static/upload/{filename}'

    return avatar_url

def login_required(view_func):
    @wraps(view_func)
    def check_session(*args, **kwargs):
        uid = session.get('uid')
        if not uid:
            return redirect('/user/login')
        else:
            return view_func(*args, **kwargs)
    return check_session
