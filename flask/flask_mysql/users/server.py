from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/process_user")
def process_user():

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)