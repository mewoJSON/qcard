from flask import Flask, render_template

# Load Instance
app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1>"