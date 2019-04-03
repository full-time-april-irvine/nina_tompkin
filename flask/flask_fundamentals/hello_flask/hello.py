from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html', phrase="hello", times=5)

@app.route('/play')
def playground():
    return render_template('playground.html')

@app.route('/play/<num>')
def playground_with_num(num):
    return render_template('many_boxes.html',times=int(num))

@app.route('/play/<num>/<color>')
def playground_with_colors(num,color):
    return render_template('many_colors.html',times=int(num),color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

@app.route("/<name>")
def hello_nina(name):
    return f"Hello {name} - you think you're SO cool, don't you?"

@app.route("/success")
def success():
    return "success!!"

@app.route("/users/<username>/<id>")
def show_user_profile(username,id):
    print(username)
    print(id)
    return "username: "+ username + ", id " + id

def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


