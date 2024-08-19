#region <PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>--|
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v---/
#region <FINAL_PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
#region <IMPORTS> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <IMPORTS> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#region <BLUEPRINT> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
#region <AUTH CALL> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v---/
auth = Blueprint('auth', __name__)
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^--\
# <AUTH CALL> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#region <ROUTES> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v---/
#region <LOGIN> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
@auth.route('/login', methods=['GET', 'POST'])
#region <FUNCTION> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Success, you are Logged In!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Failure, incorrect inputs please try again.', category='warning')
        else:
            flash('Failure, that email is connected to an account.', category='warning')
    
    return render_template('login.html', user=current_user)
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <FUNCTION> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <LOGIN> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#region <LOGOUT> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
@auth.route('/logout')
@login_required
#region <FUNCTION> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <FUNCTION> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <LOGOUT> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#region <SIGN UP> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
@auth.route('/sign-up', methods=['GET', 'POST'])
#region <FUNCTION> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Failure, this email is already attached to another account.', category='warning')
        elif len(email) < 4:
            flash('Email is too short, must be longer than 4 characters', category='warning')
        elif len(first_name) < 2:
            flash('First Name is too short, must be longer than 2 characters', category='warning')
        elif password1 != password:
            flash('Passwords do not match, try again', category='warning')
        elif len(password1) < 7:
            flash('Password is too short, must be longer than 7 characters', category='warning')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='pbkdf2', salt_length=16))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account was successfully created, welcome!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <FUNCTION> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <SIGN UP> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^--\
# <ROUTES> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <BLUEPRINT> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <FINAL_PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
#^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>--|
