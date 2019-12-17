from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")


class PasswordForm(FlaskForm):
    current_password = PasswordField('Current Password<span class="red-text">*</span>', validators=[DataRequired()])
    new_password = PasswordField('New Password<span class="red-text">*</span>', validators=[DataRequired()])
    confirm_new_password = PasswordField('Confirm New Password<span class="red-text">*</span>',
                                     validators=[DataRequired(), EqualTo("new_password")])
    submit = SubmitField("Update Password")     
