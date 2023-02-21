from flask import Flask
from webpersonal.views import base
from webpersonal.project.views import project
app= Flask(__name__)

app.register_blueprint(base)
app.register_blueprint(project)

#import webpersonal.views