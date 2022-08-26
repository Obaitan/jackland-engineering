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
    title = 'Our Services > Construction'
    return render_template('main/construction.html', title=title)


@bp.route('/services/real-estate')
def real_estate():
    title = 'Our Services > Real Estate'
    return render_template('main/real-estate.html', title=title)


@bp.route('/projects')
def projects():
    title = 'Our Projects'
    return render_template('main/projects.html', title=title)


@bp.route('/services/procurement-and-supply')
def procurement():
    title = 'Sevices > Procurement & Supply'
    return render_template('main/procurement.html', title=title)


@bp.route('/services/procurement-and-supply/component/<name>')
def component(name):
    title = "Procurement & Supply > Engineering Components"
    return render_template('main/component-single.html', title=title)


@bp.route('/services/procurement-and-supply/material/<name>')
def material(name):
    title = "Procurement & Supply > Engineering Materials"
    return render_template('main/material-single.html', title=title)