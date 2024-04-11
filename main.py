from flask import Flask, render_template, redirect, url_for, request, session
from utils.users_db import *
from errors.handlers import *
from utils.game_status import *

# Load Instance
app = Flask(__name__)

# Initialize root page
@app.route('/')
def index():
    return redirect(url_for("home"), code=302)

@app.route('/sign', methods=['GET','POST'])
def sign():
    if request.method == "POST":
        insert_user(request.form["user"], request.form["pswd"], request.form["email"])
        # If POST, send data to database
    else:
        return render_template("sign.html", code=302)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

<<<<<<< HEAD
        if user_in_database(email):
=======
    # this is messy, to-do
        if user_in_database(email) == True:
>>>>>>> e75875bc36ff8cbde355c1709c5fcf17dc3523c4
            if password_check(email, password):
                return redirect(url_for('home'))   
            else:
                return render_template("log.html", msg="Password is wrong")
        else:
            return render_template("log.html", msg="User does not exist")
    else:
        return render_template("log.html", code=302)
    
@app.route('/home')
def home():
    return render_template("game.html")


@app.route('/game')
def game():
    idx = 0
    game_info = get_game_array()
    question, answer, image = generate_question(game_info[0])
    


if __name__ == "__main__":
    app.run(debug=True)
