from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = "Topsecret"

#function that establishes the start of the session and marks gold at zero
def bootup():
    session['visits'] = 1
    session['your_gold'] = 0
    return session['visits'],session['your_gold']

@app.route('/')
def homepage():
    if 'visits' in session:
        print("*"*50)
        session['visits'] += 1
        print(f"The session count is currently {session['visits']}")
        print(f"The gold count is currently {session['your_gold']}")
        print("*"*50)
    else:
        session['visits'], session['your_gold'] = bootup()
        print("*"*50)
        print(session['your_gold'])
        print("*"*50)
    return render_template('index.html',your_gold=session['your_gold'])

@app.route('/process_money',methods=['POST'])
def process_form():
    print("*"*50+"\n"+"I'm redirecting!!"+"\n"+"*"*50)
    
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_all():
    session.pop('visits')
    session.pop('your_gold')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)