from flask import Flask, render_template, redirect, url_for, request, session
from utils.users_db import *
from errors.handlers import *


# Load Instance
app = Flask(__name__)

# Root points to login page
@app.route('/')
def index():
    return redirect(url_for("login"), code=302)

# Sign page using the methods get and post
@app.route('/sign', methods=['GET','POST'])
def sign():
    if request.method == "POST":
        insert_user(request.form["user"], request.form["pswd"], request.form["email"]) # publishes user information to database
    else:
        return render_template("sign.html", code=302) # keep page up until post request is called

# Login page
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        # Collect user information
        email = request.form["email"]
        password = request.form["password"]
        
        return redirect(url_for('home'))
        # for debugging purposes this has been ommited.   
        # checks if the password are correct. 
        if user_in_database(email):
            if password_check(email, password):
                return redirect(url_for('home'))   
            else:
                return render_template("log.html", msg="Password is wrong")
        else:
            return render_template("log.html", msg="User does not exist")
    else:
        return render_template("log.html", code=302)
    
# Demo content
# Included for demonstration purposes
@app.route('/home')
def home():
    return render_template("demo2.html")

@app.route('/assignment_one')
def assignment_one():
    return render_template("demo1.html")

# Run application
if __name__ == "__main__":
    app.run(debug=True)
