from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
from filters import time_formatter
import re
app = Flask(__name__)
app.secret_key="Topsecret"
app.jinja_env.filters['time_formatter'] = time_formatter
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
    if len(request.form["first"]) < 2:
        errors.append("First name cannot be left blank.")
    #last name must be longer than one character
    if len(request.form["last"]) < 2:
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
    query = "SELECT id, first_name, pw_hash FROM users WHERE email = %(em)s;"
    data = {
        "em":request.form["email"]
    }
    matching_users = mysql.query_db(query,data)
    if matching_users:
        user = matching_users[0]
        if bcrypt.check_password_hash(user['pw_hash'],request.form['password']):
            session["user_id"] = user["id"]
            session["user_name"] = user["first_name"]
            return redirect("/wall")
    
    flash("Email or password invalid","login")
    return redirect('/')

@app.route("/wall")
def wall():
    #Return a count of all the messages that have been sent to you
    mysql = connectToMySQL("private_wall")
    query = "SELECT COUNT(*) FROM messages WHERE recipient_id = %(id)s;"
    data = {
        "id":session["user_id"]
    }
    received_count = mysql.query_db(query,data)
    session["received_count"] = received_count[0]['COUNT(*)']
    
    #Return a count of all messages you've sent so far
    mysql = connectToMySQL("private_wall")
    query = "SELECT COUNT(*) FROM messages WHERE author_id = %(id)s;"
    data = {
        "id":session["user_id"]
    }
    sent_count = mysql.query_db(query,data)
    session["sent_count"] = sent_count[0]['COUNT(*)']
    
    # Grab sender name, message content, and age of message for all messages sent to us (i.e. sent to our currently logged-in user)
    #We will use this information to generate a list of all messages we've received.
    mysql = connectToMySQL("private_wall")
    query = "SELECT messages.id, messages.author_id, users.first_name, messages.content, messages.created_at FROM messages JOIN users ON messages.author_id = users.id WHERE recipient_id=%(current_user)s ORDER BY users.first_name;"
    data = {
        "current_user":session["user_id"]
    }
    all_your_messages = mysql.query_db(query,data)
    # Grab info about all users that are not us (i.e. that are not our currently logged-in user).
    # We will use this information to generate a list of users who we can send messages to.
    mysql = connectToMySQL("private_wall")
    query = "SELECT id, first_name FROM users WHERE NOT id=%(current_user)s ORDER BY first_name;"
    data = {
        "current_user":session["user_id"]
    }
    other_users = mysql.query_db(query,data)

    #Grab the age of all messages and format them appropriately
    return render_template("wall.html",your_messages=all_your_messages,all_users=other_users)

@app.route("/send_message", methods=["POST"])
def send_message():
    if len(request.form["content"]) < 5:
        flash("Message must be longer than 5 characters.","wall")  
        return redirect("/wall")
    #Insert new message content into database
    mysql = connectToMySQL("private_wall")
    query = "INSERT INTO messages (author_id, recipient_id, content, created_at, updated_at) VALUES (%(id)s,%(recipient)s,%(content)s,NOW(),NOW());"
    data = {
        "id":session["user_id"],
        "recipient":request.form["recipient_id"],
        "content":request.form["content"]
    }
    #the statement below returns the recipient_id, which we don't really need for anything, so we don't need a variable for it.
    mysql.query_db(query,data)
    flash("Message successfully sent!","wall")
    return redirect("/wall")

@app.route("/delete", methods=["POST"])
def delete_message():
    #Run a query that deletes the message that you clicked on
    mysql=connectToMySQL("private_wall")
    query = "DELETE FROM messages WHERE id = %(message_id)s;"
    data = {
        #The delete button used POST to send the message id to this route
        "message_id":request.form["delete"]
    }
    mysql.query_db(query,data)
    flash("Message successfully deleted.","message_list")
    return redirect("/wall")


@app.route("/logout")
def logout():
    session.clear();
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)