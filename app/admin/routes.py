# from crypt import methods
from app.admin import bp
from flask import render_template, request, flash, redirect, url_for

from app.admin.forms import LoginForm


@bp.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Admin Login'
    form = LoginForm()
    return render_template('admin/login.html', title=title, form=form)