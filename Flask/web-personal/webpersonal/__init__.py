from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#Configuracion de Flask
app= Flask(__name__)

#Configuracion en Modo Development desde el archivo config.py
#app.config.from_object('config.DevelopmentConfig')
app.config.from_object('config.DevelopmentConfig')

db =SQLAlchemy(app)

#registrando los Blueprints para el manejo de las vistas
from webpersonal.views import base
from webpersonal.project.views import project

app.register_blueprint(base)
app.register_blueprint(project)

with app.app_context():
    db.create_all()
#import webpersonal.views