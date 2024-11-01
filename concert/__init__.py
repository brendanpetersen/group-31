import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import datetime

db = SQLAlchemy()

def create_app(template_folder='templates'):
    template_folder_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    print("Creating app with template folder:", template_folder)
    
    app = Flask(__name__, template_folder=template_folder_path)

    # Register Blueprints
    from . import views
    app.register_blueprint(views.mainbp)

    from . import upcoming_concerts
    app.register_blueprint(upcoming_concerts.eventbp)

    from . import auth
    app.register_blueprint(auth.authbp)

    # Initialize Bootstrap
    bootstrap = Bootstrap(app)

    # initialise the login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # create a function that takes userid and returns User
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.scalar(db.select(User).where(User.id==user_id))

    Bcrypt(app)

    app.secret_key = 'pecanpie'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///concertdb.sqlite'
    db.init_app(app)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html", error=e)

    @app.errorhandler(500)
    def server_error(e):
        return render_template("500.html", error=e)
    
    @app.context_processor
    def get_context():
      year = datetime.datetime.today().year
      return dict(year=year)

    return app