from flask import render_template, Blueprint
#from webpersonal.project.models import PROYECTS
from webpersonal.project.models import Project
from webpersonal import db

project =Blueprint('project', __name__)

@project.route('/projects')
@project.route('/projects/index')
def index():
    projects = Project.query.all()
    db.session.commit()
    #return render_template('project/index.html', projects=PROYECTS)
    return render_template('project/index.html', projects=projects)