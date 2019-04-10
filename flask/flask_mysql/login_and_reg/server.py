from flask import Flask, render_template, request, redirect, flash, session
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = "Topsecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_user', methods=["POST"])
def process_user():
    is_valid = True
    if(len(request.form["first"])) < 1:
        flash("First name must contain at least two letters and contain only letters")
        is_valid = False
    if(len(request.form["last"])) < 1:
        flash("Last name must contain at least two letters and contain only letters.")
        is_valid = False
    if not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email address.")
        is_valid = False
    if(len(request.form["password1"])) < 8:
        flash("Password must contain a number, a capital letter, and be between 8-15 characters.")
        is_valid = False
    if(len(request.form["password1"])) > 15:
        flash("Password must contain a number, a capital letter, and be between 8-15 characters.")
        is_valid = False
    if(request.form["password1"]) != (request.form["password2"]):
        flash("Confirmation password does not match.")
        is_valid = False
    if not is_valid:
        return redirect("/")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form["password1"])
        print("*"*50)
        print(pw_hash)
        print("*"*50)
        mysql = connectToMySQL("login_and_reg")
        query = "INSERT INTO users (first_name, last_name, email, password_hash, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(em)s, %(password_hash)s, NOW(), NOW());"
        data = {
            "fname":request.form["first"],
            "lname":request.form["last"],
            "em":request.form["email"],
            "password_hash":pw_hash 
            }
        new_user = mysql.query_db(query,data)
        print("*"*50)
        print(new_user)
        print("*"*50)
        return redirect("/success")

@app.route("/success")
def success():
    print("Hello world")
    return render_template("success.html")

@app.route("/login", methods=["POST"])
def login():
    mysql = connectToMySQL("login_and_reg")
    query = "SELECT * FROM users WHERE email = %(em)s;"
    data = { "em":request.form["email"] }
    result = mysql.query_db(query,data)
    if len(result) > 0:
        if bcrypt.check_password_hash(result[0]["password"],request.form["password1"]):
            session["userid"] = result[0]["id"]
            return redirect("/success")
    flash("You could not be logged in")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)