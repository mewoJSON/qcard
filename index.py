from flask import Flask, render_template

# Load Instance
app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

#INVALID URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#SERVER ERROR
@app.errorhandler(505)
def page_not_found(e):
    return render_template("505.html"), 505