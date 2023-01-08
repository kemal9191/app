from datetime import datetime
from flask import current_app
from app import db, login_manager
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import ARRAY



@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(admin_id)


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    contents = db.relationship('Content', backref='admin', lazy=True)


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(), nullable=False)
    title = db.Column(db.String(), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    date_last_modified = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    subjects = db.Column(ARRAY(db.String()), nullable=False)
    content = db.Column(db.Text, nullable=False)
    seo_statement = db.Column(db.String())
    seo_keywords = db.Column(db.String())
    image = db.Column(db.String())
    image_str = db.Column(db.String())
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)


class FormRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    subject = db.Column(db.String(), nullable=False)
    message = db.Column(db.String(), nullable=False)
    

