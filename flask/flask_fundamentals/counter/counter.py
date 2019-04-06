from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key:"trying something out"
app.count = 0

@app.route('/')
def index_count():
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/destroy', methods=['POST'])
def destroy_count():
    session['count'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)