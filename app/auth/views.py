# third party libraries
from flask import render_template, flash

# local imports
from .forms import RegistrationForm
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
                    password_hash=form.password.data)
        print(user)
        db.session.add(user)
        db.session.commit()
        flash('te has registrado correctamente')
        print('te has registrado correctamente')
        return 'you have logged in'

    print(form.errors)
    return render_template('auth/signup.html', form=form, title='Signup')