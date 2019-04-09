from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key="ThisIsTopSecret"

@app.route('/')
def index():
    mysql = connectToMySQL("first_flask")
    friends = mysql.query_db("SELECT * FROM friends;")
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route("/create_friend",methods=["POST"])
def add_friend_to_db():
    is_valid = True
    if len(request.form['fname']) < 1:
        flash("Please enter a valid first name")
        is_valid = False
    if len(request.form['lname']) < 1:
        flash("please enter a valid last name")
        is_valid = False
    if len(request.form['occ']) < 2:
        flash("Occupation should be at least 2 characters")
        is_valid = False
    if not is_valid:
        return redirect('/')
    else:
        mysql = connectToMySQL('first_flask')
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fn)s, %(ln)s,%(occup)s,NOW(),NOW());"
        data = {
            "fn":request.form["fname"],
            "ln":request.form["lname"],
            "occup":request.form["occ"]
        }
        db = connectToMySQL("first_flask")
        new_friend_id = mysql.query_db(query,data)
        return redirect("/success")

@app.route("/success")
def success():
    print("Hello mofos")

if __name__ == "__main__":
    app.run(debug=True)