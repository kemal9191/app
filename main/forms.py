from tokenize import String
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, FileField, SelectField,SelectMultipleField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class ContactForm(FlaskForm):
    name = StringField('Name*', validators=[DataRequired()])
    email = StringField('Email*', validators=[DataRequired(), Email()])
    subject = StringField('Subject*', validators=[DataRequired()])
    message = TextAreaField('Message*', validators=[DataRequired()])
    submit = SubmitField('SEND MESSAGE')