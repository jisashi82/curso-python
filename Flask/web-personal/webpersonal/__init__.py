from flask import Flask
from webpersonal.views import base

app= Flask(__name__)

app.register_blueprint(base)

#import webpersonal.views