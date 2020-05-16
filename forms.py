from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

# Login Form


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=3, max=15)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=3, max=15)])
    submit = SubmitField('Login')
