from flask import Flask, render_template, redirect, url_for, request
from utils.database import insert_user, user_in_database, password_check

# Load Instance
app = Flask(__name__)

# Initialize root page
@app.route('/')
def index():
    return redirect(url_for("sign"), code=302)

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

    # this is messy, to-do
        if user_in_database(email) == True:
            if password_check(email, password):
                return f"<h1>Welcome {email} </h1>"
            else:
                return render_template("log.html", msg="Password is wrong")
        else:
            return render_template("log.html", msg="User does not exist")
    else:
        return render_template("log.html", code=302)

if __name__ == "__main__":
    app.run(debug=True)