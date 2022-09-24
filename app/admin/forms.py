from datetime import datetime
# from collections import Iterable
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateField, FileField
# from wtforms.fields import TelField
from wtforms.validators import DataRequired, Email, ValidationError
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Project
# from werkzeug.datastructures import FileStorage


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    

class NewProjectForm(FlaskForm):        
    def validate_title(self, title):
        title_dup = Project.query.filter_by(title=title.data).first()
        if title_dup:
            raise ValidationError(
                "Project titles must be unique! This title already exists."
            )
                
    title = StringField(label="Title", validators=[DataRequired()])
    description = TextAreaField("Desciption", validators=[DataRequired()])
    location = StringField(label="Location", validators=[DataRequired()])
    budget = StringField(label="Budget", validators=[DataRequired()])
    start_year = DateField("Start Year", [DataRequired()])
    duration = StringField(label="Duration in Months", validators=[DataRequired()])
    client = StringField(label="Client", validators=[DataRequired()])
    pix = StringField(label="Images", validators=[DataRequired()])
    submit = SubmitField("Add Project")


# class EditProjectForm(FlaskForm):           
#     title = StringField(label="Project Name", validators=[DataRequired()])
#     description = TextAreaField("Project Desciption", validators=[DataRequired()])
#     location = StringField(label="Project Location", validators=[DataRequired()])
#     budget = StringField(label="Budget", validators=[DataRequired()])
#     start_year = DateField("Start Year", [DataRequired()])
#     duration = StringField(label="Duration in Months", validators=[DataRequired()])
#     images_caption = StringField(label="Images Caption", validators=[DataRequired()])
#     pix1 = URLField("Image Link 1", validators=[DataRequired(), URL()])
#     pix2 = URLField("Image Link 2", validators=[DataRequired(), URL()])
#     pix3 = URLField("Image Link 3", validators=[DataRequired(), URL()])
#     pix4 = URLField("Image Link 4", validators=[Optional(), URL()])
#     pix5 = URLField("Image Link 5", validators=[Optional(), URL()])
#     pix6 = URLField("Image Link 6", validators=[Optional(), URL()])
#     submit = SubmitField("Update Project")


class NewMaterialForm(FlaskForm):        
    def validate_name(self, name):
        name_dup = Project.query.filter_by(name=name.data).first()
        if name_dup:
            raise ValidationError(
                "Material names must be unique! This name already exists."
            )
        
    name = StringField(label="Material Name", validators=[DataRequired()])
    uses = TextAreaField("Uses", validators=[DataRequired()])
    doc = FileField("Tech Sheet", validators=[DataRequired()])
    images = StringField("Images", validators=[DataRequired()])  
    submit = SubmitField("Add Material")



class NewEquipmentForm(FlaskForm):        
    def validate_name(self, name):
        name_dup = Project.query.filter_by(name=name.data).first()
        if name_dup:
            raise ValidationError(
                "Material names must be unique! This name already exists."
            )
        
    name = StringField(label="Equipment Name", validators=[DataRequired()])
    doc = FileField("Tech Sheet", validators=[DataRequired()])
    images = StringField("Images", validators=[DataRequired()])  
    submit = SubmitField("Add Equipment")


# class ContactForm(FlaskForm):
#     name = StringField("Full Name", validators=[DataRequired()])
#     phone = TelField("Phone Number", validators=[DataRequired()])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     message = TextAreaField("Message", validators=[DataRequired()])
#     submit = SubmitField("Send Message")