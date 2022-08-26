from datetime import datetime
# from collections import Iterable
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# from wtforms.fields import TelField
# from wtforms.fields import URLField, DateField
from wtforms.validators import DataRequired, Email
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
# from app.models import Project, User
# from werkzeug.datastructures import FileStorage


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Login")