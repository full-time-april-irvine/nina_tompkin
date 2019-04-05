from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="woh;lakjsd;fjset"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def show_results():
    #deal with form info
    session['user_name']=request.form["user_name"]
    session['dojo_locations']=request.form["dojo_locations"]
    session['fav_lang']=request.form["fav_lang"]
    session['comment_content']=request.form["comment"]
    return redirect('/success')
    
@app.route("/success")
def success():
    print(request.form)
    return render_template("results.html",
    fullname=session['user_name'],
    dojolocation=session['dojo_locations'],
    favoritelang=session['fav_lang'],
    comment_content=session['comment_content'])

if __name__ == "__main__":
    app.run(debug=True)