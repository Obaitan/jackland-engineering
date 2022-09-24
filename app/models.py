from datetime import datetime
from enum import unique
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    email = db.Column(db.String(100), index=True, nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<User: {self.name}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, index=True, nullable=False, unique=True)
    description = db.Column(db.Text, index=True, nullable=False, unique=False)
    location = db.Column(db.String(50), index=True, nullable=False, unique=False)
    budget = db.Column(db.String(15), index=True, nullable=False, unique=False)
    duration = db.Column(db.String(3), index=True, nullable=False, unique=False)
    client = db.Column(db.Text, index=True, nullable=False, unique=False)
    start_year = db.Column(db.DateTime, index=True, nullable=False, unique=False)
    images = db.relationship('Image', backref='project_image', lazy='dynamic')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Project: {self.title}>'


class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    properties = db.Column(db.Text, index=True, nullable=False, unique=False)
    uses = db.Column(db.Text, index=True, nullable=False, unique=False)
    images = db.relationship('Image', backref='material_image', lazy='dynamic')
    doc = db.relationship('Sheet', backref='material_sheet', lazy='dynamic')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Material: {self.name}>'


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False, unique=True)
    properties = db.Column(db.Text, index=True, nullable=False, unique=False)
    images = db.relationship('Image', backref='equipment_image', lazy='dynamic')
    doc = db.relationship('Sheet', backref='equipment_sheet', lazy='dynamic')
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Equipment: {self.name}>'
    

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pix = db.Column(db.String, index=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'))
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    
    def __repr__(self):
        return f'<Project: {self.id}>'


class Sheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doc = db.Column(db.String, index=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'))
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    
    def __repr__(self):
        return f'<Project: {self.id}>'
