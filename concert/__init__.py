import os
from flask import Flask, render_template

def create_app(template_folder='templates'):
    template_folder_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    print("Creating app with template folder:", template_folder)
    app = Flask(__name__, template_folder=template_folder_path)
    from . import views
    app.register_blueprint(views.mainbp)

    app.secret_key = 'pecanpie'

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html", error=e)

    @app.errorhandler(500) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("500.html", error=e)
    return app

