from flask import render_template, Blueprint

project =Blueprint('project', __name__)

@project.route('/projects')
def projects():
    return 'Pagina de Proyectos'