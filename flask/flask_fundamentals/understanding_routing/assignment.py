from flask import Flask 
app = Flask(__name__)
@app.route('/')          
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def success():
    return "Dojo!"

@app.route("/say/<name>")
def show_user_profile(name):
    return "Hi "+ name + "!"

@app.route("/repeat/<num>/<word>")
def repeat_after_me(num,word):
    var = int(num)
    my_str = ""
    for i in range(var):
        my_str += f"{word} \n"
    return my_str

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

