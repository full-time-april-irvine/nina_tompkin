from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key="Topsecret"

@app.route("/users")
def index():
    mysql = connectToMySQL("users_cd")
    users = mysql.query_db("SELECT * FROM friends;")
    print(users)
    return render_template("users.html",all_users=users)

@app.route("/users/new")
def add_users():
    return render_template("new.html")

@app.route("/users/<idnum>")
def show_user(idnum):
    mysql = connectToMySQL("users_cd")
    query = "SELECT * FROM friends WHERE id= %(user_id)s;"
    data = {
        "user_id":idnum
    }
    user = mysql.query_db(query,data)
    return render_template("one_user.html",current_user=user[0])

@app.route("/users/<idnum>/edit")
def edit_user(idnum):
    return render_template("update.html",current_user_id=idnum)

@app.route("/<idnum>/update_user",methods=['POST'])
def update_user(idnum):
    mysql = connectToMySQL("users_cd")
    query = "UPDATE friends SET first_name = %(fname)s, last_name=%(lname)s, email=%(email)s WHERE id =%(user_id)s;"
    data = {
        "fname":request.form["first"],
        "lname":request.form["last"],
        "email":request.form["email"],
        "user_id":idnum
    }
    mysql.query_db(query,data)
    return redirect("/users/" + idnum)

@app.route("/process_user", methods=['POST'])
def process_user():
    mysql = connectToMySQL("users_cd")
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s,%(lname)s,%(email)s,NOW(),NOW());"
    data = {
        "fname":request.form["first"],
        "lname":request.form["last"],
        "email":request.form["email"],
    }
    new_user_id = mysql.query_db(query,data)
    return redirect("/users/" + str(new_user_id))

@app.route("/delete_user<idnum>")
def delete_user(idnum):
    mysql = connectToMySQL("users_cd")
    query = "DELETE FROM friends WHERE id = %(id)s;"
    data = {
        "id":int(idnum)
    }
    mysql.query_db(query,data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)