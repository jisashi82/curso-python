from flask import render_template, Blueprint, request,redirect,url_for
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

@project.route('/projects/create')
def create():
    return render_template('project/create.html')

@project.route('/projects/insert', methods=['POST'])
def insert():
    title = request.form.get('title')
    description = request.form.get('description')
    
    project= Project(title,description)
    
    db.session.add(project)
    db.session.commit()
    
    return redirect(url_for('project.index'))

@project.route('/projects/edit/<int:id>')
def edit(id):
    project = Project.query.get_or_404(id)
    return render_template('project/edit.html', p=project)