from flask import render_template, Blueprint

# Handles error and displays error page according to the computer network communication error
errors = Blueprint('errors', __name__)

# Catches exception, loads error page from the errors folder
# pre-req: error (int)
# post-req: renders a template (website)
@errors.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404

@errors.errorhandler(505)
def page_not_found(e):
    return render_template("errors/505.html"), 505