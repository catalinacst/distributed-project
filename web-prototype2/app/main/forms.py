from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField
from wtforms.validators import Required, DataRequired, EqualTo
#from flask_wtf import FlaskForm as BaseForm


class LoginForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('', validators=[Required()])
    room = StringField('')
    submit = SubmitField('')


class RegistrationForm(FlaskForm):
    """Accepts a nickname and a room."""
    first_name = StringField('', validators=[Required()])
    last_name = StringField('', validators=[Required()])
    username = StringField('', validators=[Required()])
    password = PasswordField('New Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    age = StringField('')
    gender = StringField('')
    submit = SubmitField('')
