from flask import Flask
app = Flask(__name__)
if __name__=="__main__":
    app.run(debug=True)

# @app.route("/")
# def hello_world():
#     return "Hello World!"

# @app.route("/dojo")
# def dojo():
#     return "Dojo!"

# @app.route("/say/<name>")
# def show_name(name):
#     return "Hi " + name + "!"
