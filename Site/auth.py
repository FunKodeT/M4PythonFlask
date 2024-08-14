################################################################>
#=========================================================>
#<PROGRAM_NAME>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM0_V0>
#=========================================================<
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## IMPORTS
#-------------------------------------<
from flask import Blueprint, render_template, request, flash
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## BLUEPRINT
#:::::::::::::::::::::::::::::::::::::<
# BLUEPRINT: AUTH
#---------------------------<
auth = Blueprint('auth', __name__)
#-------------------------------------<
# BLUEPRINT: ROUTES
#---------------------------<
#region <LOGIN ROUTE>
#---------------<
@auth.route('/login', methods=['GET', 'POST'])
#---------------<
# LOGIN: FUNCTION
#----------<
def login():
    return render_template('login.html', boolean=True)

#endregion
#---------------------------<
#region <LOGOUT ROUTE>
#---------------<
@auth.route('/logout')
#---------------<
# LOGOUT: FUNCTION
#----------<
def logout():
    return '<p>Logout</p>'

#endregion
#---------------------------<
#region <SIGN-UP ROUTE>
#---------------<
@auth.route('/sign-up', methods=['GET', 'POST'])
#---------------<
# SIGN-UP: FUNCTION
#----------<
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password = request.form.get('password')
        if len(email) < 4:
            flash('Email is too short, must be longer than 4 characters', category='warning')
            pass
        elif len(firstName) < 2:
            pass
            flash('First Name is too short, must be longer than 2 characters', category='warning')
        elif password1 != password:
            pass
            flash('Passwords do not match, try again', category='warning')
        elif len(password1) < 7:
            pass
            flash('Password is too short, must be longer than 7 characters', category='warning')
        else:
            flash('Account was successfully created, welcome!', category='success')

    return render_template('sign_up.html')

#endregion
#:::::::::::::::::::::::::::::::::::::::::::::::<
#=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>