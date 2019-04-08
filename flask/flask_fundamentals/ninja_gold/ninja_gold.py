from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask (__name__)
app.secret_key = "Topsecret"

#function that accepts two arguments to generate a random number
def randomNum(start,end):
    random_num = random.randint(start,end)
    return random_num

def profit_or_loss(num):
    buildingInput = session["building"]
    if num > 0:
        session['your_gold'] += num
        session['phrase'] = f"Earned {num} golds from the {buildingInput}!"
    else:
        session['your_gold'] += num
        session['phrase'] = f"Entered a {buildingInput} and lost {num} golds...Ouch..."
    return session['phrase']

#function that establishes the start of the session and marks gold at zero
def bootup():
    session['visits'] = 1
    session['your_gold'] = 0
    return session['visits'],session['your_gold']

@app.route('/')
def homepage():
    if 'visits' in session:
        buildingInput = session["building"]
        if buildingInput == "farm":
            profit = randomNum(10,20)
            activity = profit_or_loss(profit)
            session['activities'].append([activity,"good"])
        elif buildingInput == "cave":
            profit = randomNum(5,10)
            activity = profit_or_loss(profit)
            session['activities'].append([activity,"good"])
        elif buildingInput == "house":
            profit = randomNum(2,5)
            activity = profit_or_loss(profit)
            session['activities'].append([activity,"good"])
        else:
            ladyluck = randomNum(0,1)
            if ladyluck == 0:
                loss = randomNum(-50,-1)
                activity = profit_or_loss(loss)
                session['activities'].append([activity,"bad"])
            else:
                profit = randomNum(1,50)
                activity = profit_or_loss(profit)
                session['activities'].append([activity,"good"])
    else:
        #to be performed only for the first round of the game. 
        session['visits'], session['your_gold'] = bootup()
        session['phrase'] = ""
        session['activities'] = []
    return render_template('index.html',
        your_gold=session['your_gold'],
        activities=session['activities'])

@app.route('/process_money',methods=['POST'])
def process_form():
    session["building"] = request.form["building"]
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_all():
    session.pop('visits')
    session.pop('your_gold')
    session.pop('phrase')
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)