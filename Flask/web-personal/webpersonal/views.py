from flask import render_template, Blueprint
#from webpersonal import app

base = Blueprint('base', __name__)

@base.route('/')
def home():
    return render_template('home.html',msj='pagina de inicio')

@base.route('/portfolio')
def portfolio():
    return render_template('portfolio.html',msj='Portfolio')

@base.route('/contact')
def contact():
    return render_template('contact.html', msj='Formulario de contacto')