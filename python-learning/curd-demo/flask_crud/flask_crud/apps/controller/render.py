from flask import Blueprint
from flask import render_template
from flask import request


# 渲染蓝图
render_blue = Blueprint('render', __name__, url_prefix='/render')


@render_blue.route('/')
def render_index():
    """
    渲染 index 页面
    """
    return render_template('index.html')


@render_blue.route('/greet', methods=['POST'])
def greet():
    """
    渲染 greet 页面
    """
    name = request.form.get('name')
    return render_template('index.html', name=name)
