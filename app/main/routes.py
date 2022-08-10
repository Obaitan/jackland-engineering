from app.main import bp
from flask import render_template, request, flash, redirect, url_for


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    title = 'Home'
    return render_template('main/index.html', title=title)


@bp.route('/about-us')
def about():
    title = 'About Us'
    return render_template('main/about.html', title=title)


@bp.route('/services/construction')
def construction():
    title = 'Services > Construction'
    return render_template('main/construction.html', title=title)