from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from libs.pas import login_required

from libs.orm import db
from weibo.models import Weibo

weibo_bp = Blueprint('weibo',
                     __name__,
                     url_prefix='/weibo',
                     template_folder='./templates'
                     )


@weibo_bp.route('/index')
def index():
    return render_template('index.html')


@weibo_bp.route('/post')
@login_required
def post():
    return render_template('post.html')


@weibo_bp.route('/read')
def read():
    return render_template('read.html')


@weibo_bp.route('/edit')
@login_required
def edit():
    return render_template('eddit.html')
