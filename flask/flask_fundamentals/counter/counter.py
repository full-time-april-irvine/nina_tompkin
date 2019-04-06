from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="trying something out"

@app.route('/')
def index_count():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html', count=session['visits'])

@app.route('/destroy', methods=['POST'])
def destroy_count():
    session.pop('visits')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)