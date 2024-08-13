################################################################>
#=========================================================>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <FINAL_PROGRAM>
#=========================================================<
## LINE FORMATS
                    #
#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
                    #
#:::::::::::::::::::::::::::::::::::::::::::::::<
                    #
#::::::::::::::::::::::::::::::::::::::::<
                    #
#:::::::::::::::::::::::::::::::<
                    #
#-------------------------------------<
                    #
#---------------------------<
                    #
#---------------<
                    #

## EXAMPLES OF FORMATTING

#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## SECTION NAME
#:::::::::::::::::::::::::::::::::::::<
# SECTION PART
#---------------------------<
# PART CODE
#-------------------------------------<
# SECTION PART
#---------------<
# PART CODE
#:::::::::::::::::::::::::::::::::::::::::::::::<


#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
## SECTION NAME
#:::::::::::::::::::::::::::::::::::::<
# SECTION PART
#---------------------------<
# PART CODE
#:::::::::::::::::::::::::::::::::::::::::::::::<



#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# SECTION NAME
#-------------------------------------<
# SECTION CODE
    #:::::::::::::::::::::::::::::::<
    # CODE PART
    #---------------<
    # PART CODE
#:::::::::::::::::::::::::::::::::::::::::::::::<



#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# SECTION NAME
#:::::::::::::::::::::::::::::::::::::<
# PART NAME
#---------------<
# SECTION CODE
#:::::::::::::::::::::::::::::::::::::<
# PART NAME
#---------------<
# SECTION CODE
#:::::::::::::::::::::::::::::::::::::<
# PART NAME
#---------------<
# SECTION CODE
#:::::::::::::::::::::::::::::::::::::::::::::::<



#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# SECTION NAME
#:::::::::::::::::::::::::::::::::::::<
# PART NAME
#---------------<
# SECTION CODE
#:::::::::::::::::::::::::::::::::::::::::::::::<



#_______________________________________________/
#:::::::::::::::::::::::::::::::::::::::::::::::\
# SECTION NAME
#-------------------------------------<
# SECTION CODE
#:::::::::::::::::::::::::::::::::::::::::::::::<



#:::::::::::::::::::::::::::::::::::::<
# PART NAME
#:::::::::::::::::::::::::::<
# NAME PURPOSE
#---------------<
# NAME CODE
#:::::::::::::::::::::::::::::::::::::::::::::::<
#=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
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
from flask import Blueprint, render_template
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
@auth.route('/login')
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
@auth.route('/sign-up')
#---------------<
# SIGN-UP: FUNCTION
#----------<
def sign_up():
    return render_template('sign_up.html')

#endregion
#:::::::::::::::::::::::::::::::::::::::::::::::<
#=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM0_V0>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from flask import Blueprint, render_template
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BLUEPRINT
# #:::::::::::::::::::::::::::::::::::::<
# # BLUEPRINT: AUTH
# #---------------------------<
# auth = Blueprint('auth', __name__)
# #-------------------------------------<
# # BLUEPRINT: ROUTES
# #---------------------------<
# #region <LOGIN ROUTE>
# #---------------<
# @auth.route('/login')
# #---------------<
# # LOGIN: FUNCTION
# #----------<
# def login():
#     return render_template('login.html', text='Testing', user='Matth')

# #endregion
# #---------------------------<
# #region <LOGOUT ROUTE>
# #---------------<
# @auth.route('/logout')
# #---------------<
# # LOGOUT: FUNCTION
# #----------<
# def logout():
#     return '<p>Logout</p>'

# #endregion
# #---------------------------<
# #region <SIGN-UP ROUTE>
# #---------------<
# @auth.route('/sign-up')
# #---------------<
# # SIGN-UP: FUNCTION
# #----------<
# def sign_up():
#     return render_template('sign_up.html')

# #endregion
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM0_V0>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from flask import Blueprint
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BLUEPRINT
# #:::::::::::::::::::::::::::::::::::::<
# # BLUEPRINT: DEFINE PAGE
# #---------------------------<
# auth = Blueprint('auth', __name__)
# #-------------------------------------<
# # BLUEPRINT: DEFINE ROUTES
# #---------------------------<
# # ROUTE: LOGIN
# #---------------<
# @auth.route('/login')
# #---------------<
# # LOGIN: FUNCTION
# #----------<
# def login():
#     return '<p>Login</p>'
# #---------------------------<
# # ROUTE: LOGOUT
# #---------------<
# @auth.route('/logout')
# #---------------<
# # LOGOUT: FUNCTION
# #----------<
# def logout():
#     return '<p>Logout</p>'
# #---------------------------<
# # ROUTE: SIGN-UP
# #---------------<
# @auth.route('/sign-up')
# #---------------<
# # SIGN-UP: FUNCTION
# #----------<
# def sign_up():
#     return '<p>Sign Up</p>'
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM0_V0>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from flask import Blueprint
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BLUEPRINT
# #:::::::::::::::::::::::::::::::::::::<
# # BLUEPRINT: DEFINE PAGE
# #---------------------------<
# auth = Blueprint('auth', __name__)
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#region <PROGRAM0_V0>
# #=========================================================<
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## IMPORTS
# #-------------------------------------<
# from flask import Blueprint
# #_______________________________________________/
# #:::::::::::::::::::::::::::::::::::::::::::::::\
# ## BLUEPRINT
# #:::::::::::::::::::::::::::::::::::::<
# # BLUEPRINT: DEFINE PAGE
# #---------------------------<
# auth = Blueprint('auth', __name__)
# #-------------------------------------<
# # BLUEPRINT: DEFINE ROUTES
# #---------------------------<
# @auth.route('hello')
# #:::::::::::::::::::::::::::::::::::::::::::::::<
# #=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
################################################################>