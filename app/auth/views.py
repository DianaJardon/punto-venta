# third party libraries
from flask import render_template, flash
from flask_login import login_required, login_user, logout_user
# local imports
from .forms import RegistrationForm, LoginForm
from ..models import User
from . import auth
from .. import db


@auth.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.errors)
    print('outside')
    if form.validate_on_submit():
        print('inside')
        user = User(user_name=form.name.data,
                    last_name=form.last_name.data,
                    user_email=form.email.data,
                    password=form.password.data)
        print(user)
        db.session.add(user)
        db.session.commit()
        flash('te has registrado correctamente')
        print('te has registrado correctamente')
        return 'you have logged in'

    print(form.errors)
    return render_template('auth/signup.html', form=form, title='Signup')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if user is not None and user.verify_password(
            form.password.data
        ):
            login_user(user)
            return 'you have logged in'
        else:
            print('Invalid email or password')
            flash('Invalid email or password')

    return render_template('auth/login.html', form=form, title='Registrarse')
