#region <PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>--|
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v---/
#region <FINAL_PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
#region <IMPORTS> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <IMPORTS> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#region <SQL> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
db = SQLAlchemy()
#region <DB_NAME> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v---/
DB_NAME = 'database.db'
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^--\
# <DB_NAME> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <SQL> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#region <FLASK> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v--/
#region <FUNCTIONS> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v---/
#region <CREATE_APP> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1qaz!QAZ2wsx@WSX'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    with app.app_context():
        db.create_all

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <CREATE_APP> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#region <CREATE_DB> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->/
#v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/v\/--/
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Success, Database Created!')
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <CREATE_DB> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^--\
# <FUNCTIONS> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <FLASK> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
# <FINAL_PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-->\
#^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^---\
#^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
#endregion ^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\^/\--\
# <PROGRAM> >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>--|