from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    user_info = [
        {'first_name':'Michael','last_name':'Choi'},
        {'first_name':'Wes','last_name':'Harper'},
        {'first_name':'Nina','last_name':'Tompkin'},
        {'first_name':'Dimitar','last_name':'Ho'},
    ]
    return render_template('index.html',users=user_info)

if __name__=="__main__":
    app.run(debug=True)