from flask import render_template, Blueprint

# Definindo o blueprint
routes = Blueprint('routes', __name__)

@routes.route('/')
@routes.route('/home')
def main():
    return render_template('home.html')

@routes.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404
