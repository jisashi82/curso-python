from flask import render_template
from webpersonal import app

@app.route('/')
def home():
    return render_template('home.html',msj='pagina de inicio')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html',msj='Portfolio')

@app.route('/contact')
def contact():
    return render_template('contact.html', msj='Formulario de contacto')