from flask import insert_error_page

@app.errorhandler(404)
def not_found(error):
    return insert_error_page('static', '404.html'), 404

@app.errorhandler(500)
def not_found(error):
    return insert_error_page('static', '500.html'), 500

