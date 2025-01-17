from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class SignupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(), Email()])
