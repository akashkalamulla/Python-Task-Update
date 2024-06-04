from wsgiref.validate import validator
from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, ValidationError

class RegistrationForm(FlaskForm):
  Username = StringField('Username',validators=[DataRequired()])
  email = StringField('Email',validators=[DataRequired(),Email()])
  phone = StringField('phone',validators=[DataRequired(),Length(min=10,max=10,message="Phone number must be 10 digits")])
  password = PasswordField('Password',validators=[DataRequired(),Regexp(regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',message="Password must be at least 8 characters long and contain both letters and numbers.")])
  confirm_password = PasswordField('Confirm_password',validators=[DataRequired(),EqualTo('Password',message="Password must match.")])
  submit = SubmitField('Register')

class LoginForm(FlaskForm):
  email_or_phone = StringField('Email or Phone',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')

def validators(self):
  if not super(LoginForm, self).validators():
    return False

  data = self.email_or_phone.data
  if not (self._is_email(data) or self._is_phone(data)):
    msg = 'Please enter a valid email or phone number.'
    self.email_or_phone.errors.append(msg)
    return False

  return True

  


