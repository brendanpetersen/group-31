import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(template_folder='templates'):
    template_folder_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    print("Creating app with template folder:", template_folder)
    app = Flask(__name__, template_folder=template_folder_path)
    from . import views
    app.register_blueprint(views.mainbp)

    from . import upcoming_concerts
    app.register_blueprint(upcoming_concerts.eventbp)

    from . import auth
    app.register_blueprint(auth.authbp)

    Bootstrap5(app)

    app.secret_key = 'pecanpie'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traveldb.sqlite'
    db.init_app(app)

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html", error=e)

    @app.errorhandler(500) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("500.html", error=e)
    return app

