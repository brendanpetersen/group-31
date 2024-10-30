from flask import Flask, show_error_page

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return show_error_page('404.html'), 404

@app.errorhandler(500)
def not_found(error):
    return show_error_page('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)