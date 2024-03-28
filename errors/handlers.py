from flask import render_template, Blueprint

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404

@errors.app_errorhandler(505)
def page_not_found(e):
    return render_template("errors/505.html"), 505