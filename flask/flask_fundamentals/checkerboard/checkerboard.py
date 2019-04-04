from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')

@app.route('/<num_rows>/<num_columns>')
def checkerboard_mult(num_rows,num_columns):
    return render_template('index.html',rows=int(num_rows),columns=int(num_columns))

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
