from flask import Flask, render_template, request, redirect, session, flash
import re
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "Topsecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_email',methods=["POST"])
def process_email():
    if not EMAIL_REGEX.match(request.form["email"]):
        flash("Email is not valid!")
        return redirect('/')
    else:
        mysql = connectToMySQL("email_val")
        query = "INSERT INTO emails (email) VALUES (%(em)s);"
        data = {
            "em":request.form["email"]
        }
        new_email = mysql.query_db(query,data)
        flash("The email address you entered ("+request.form["email"]+") is a VALID email address! Thank you!")
        return redirect('/success')

@app.route('/success')
def success():
    mysql = connectToMySQL("email_val")
    users = mysql.query_db("SELECT * FROM emails;")
    return render_template("success.html", all_users=users)

if __name__ == "__main__":
    app.run(debug=True)