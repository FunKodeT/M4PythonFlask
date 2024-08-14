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
# BLUEPRINT: DEFINE PAGE
#---------------------------<
views = Blueprint('views', __name__)
#-------------------------------------<
# BLUEPRINT: DEFINE ROUTES
#---------------------------<
@views.route('/')
#-------------------------------------<
# ROUTE: HOME
#---------------------------<
def home():
    return render_template('home.html')
#:::::::::::::::::::::::::::::::::::::::::::::::<
#=========================================================<
#endregion
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
#=========================================================>
#################################################################