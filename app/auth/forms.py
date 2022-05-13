# third part imports
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

# local import
from ..models import User


class RegistrationForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellido')
    email = StringField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirmar Constraseña', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

    @staticmethod
    def validate_email(self, email):
        if User.query.filter_by(user_email=email.data).first():
            raise ValidationError('Email is already in use')


class LoginForm(FlaskForm):
    email = StringField('Correo', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesion')