from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello():
    return "Hello!!"

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

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
