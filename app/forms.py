from flask_wtf import FlaskForm
from wtforms import HiddenField, IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError
import sqlalchemy as sa
from app import db
from .models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')


class AddBook(FlaskForm):
    id_field = HiddenField()
    title = StringField('Book title', validators=[DataRequired()])
    author = StringField('Author Name', validators=[DataRequired()])
    publication_year = IntegerField(
        'Publication Year', validators=[DataRequired()])

    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')
