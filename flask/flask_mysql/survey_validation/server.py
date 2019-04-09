from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key="Topsecret"

@app.route('/')
def index():
    print("Hello world!")
    return render_template('index.html')

@app.route("/process_entry", methods=["POST"])
def process_entry():
    is_valid = True
    if len(request.form["user_name"]) < 1:
        flash("Please enter a valid name. Name must be more than one character.")
        is_valid = False
    if len(request.form["comment"]) > 120:
        flash("Please limit your comment to 120 characters or less.")
        is_valid = False
    if request.form["dojo_locations"] == "blank":
        flash("Please select your location from the dropdown.")
        is_valid = False
    if request.form["fav_lang"] == "blank":
        flash("Please select your favorite language from the dropdown.")
        is_valid = False
    if not is_valid:
        return redirect('/')
    else:
        mysql = connectToMySQL("dojo_survey")
        query = "INSERT INTO users (name, dojo_location, fav_lang, comment, created_at, updated_at) VALUES (%(n)s, %(dojo)s, %(lang)s, %(comment)s, NOW(), NOW());"
        data = {
            "n":request.form["user_name"],
            "dojo":request.form["dojo_locations"],
            "lang":request.form["fav_lang"],
            "comment":request.form["comment"]
        }
        new_user_id = mysql.query_db(query,data)
        session['recent_user'] = new_user_id
        print("*"*50)
        print(new_user_id)
        print("*"*50)
        return redirect('/success')

@app.route("/success")
def success():
    mysql = connectToMySQL("dojo_survey")
    query = mysql.query_db("SELECT * FROM users WHERE id = %(id)s;")
    data = {
        "id":session['recent_user']
    }
    user = mysql.query_db(query,data)
    return render_template('/success', new_user=user[0])

if __name__ == "__main__":
    app.run(debug=True)