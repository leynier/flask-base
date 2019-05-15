from flask import render_template
from . import main_blueprint


@main_blueprint.route('/')
def index():
    return render_template('index.html')


@main_blueprint.app_errorhandler(403)
@main_blueprint.app_errorhandler(404)
@main_blueprint.app_errorhandler(500)
def errors(e):
    return render_template(f'errors/{e.code}.html'), e.code
