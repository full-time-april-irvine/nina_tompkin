from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key="Topsecret"
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,16}$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def register_user():
    errors = []
    #first name must be longer than one character
    if len(request.form["first"]) < 1:
        errors.append("First name cannot be left blank.")
    #last name must be longer than one character
    if len(request.form["last"]) < 1:
        errors.append("Last name cannot be left blank.")
    #email must be in a valid format
    if not EMAIL_REGEX.match(request.form["email"]):
        errors.append("Email must be in a valid format")
    #email must be unique
    mysql = connectToMySQL("private_wall")
    query = "SELECT * FROM users WHERE email = %(em)s;"
    data = {
        "em":request.form["email"]
    }
    matching_users = mysql.query_db(query,data)
    if matching_users:
        errors.append("Email already in use")
    #password must contain at least one uppercase letter, one number and be between 8 and 15 characters long.
    if not PASSWORD_REGEX.match(request.form["password"]):
        errors.append("Password must contain one uppercase letter, a number, and be between 8 and 15 characters.")
    #password must match password confirmation
    if request.form["password"] != request.form["password2"]:
        errors.append("Password confirmation does not match password.")
    if errors:
        for error in errors:
            flash(error, "register")
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    mysql = connectToMySQL("private_wall")
    query = "INSERT INTO users (first_name, last_name, email, pw_hash) VALUES (%(fname)s,%(lname)s,%(em)s,%(pw)s);"
    data = {
        "fname":request.form["first"],
        "lname":request.form["last"],
        "em":request.form["email"],
        "pw":pw_hash
    }
    user_id = mysql.query_db(query,data)
    session["user_id"] = user_id
    return redirect("/")

@app.route("/login", methods =["POST"])
def login():
    mysql = connectToMySQL("private_wall")
    query = "SELECT id, pw_hash FROM users WHERE email = %(em)s;"
    data = {
        "em":request.form["email"]
    }
    matching_users = mysql.query_db(query,data)
    if matching_users:
        user = matching_users[0]
        if bcrypt.check_password_hash(user['pw_hash'],request.form['password']):
            session["user_id"] = user["id"]
            return redirect("/wall")
    
    flash("Email or password invalid","login")
    return redirect('/')

@app.route("/wall")
def wall():
    return render_template("wall.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    if len(request.form["content"]) < 5:
        flash("Message must be longer than 5 characters.","wall")  
    return redirect("/wall")

    mysql = connectToMySQL("private_wall")
    query = "INSERT INTO messages (user_id, content, created_at, updated_at) VALUES (%(id)s,%(content)s,NOW(),NOW());"
    data = {
        "id":session["user_id"],
        "content":request.form["content"]
    }
    mysql.query_db(query,data)
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear();
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)