from flask import render_template, Blueprint
#from webpersonal.project.models import PROYECTS
from webpersonal.project.models import Project

project =Blueprint('project', __name__)

@project.route('/projects')
@project.route('/projects/index')
def index():
    #return render_template('project/index.html', projects=PROYECTS)
    return 'Cargar Modelo'