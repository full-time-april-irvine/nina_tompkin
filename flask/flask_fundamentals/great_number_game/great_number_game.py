from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "TopSecret"

@app.route('/')
def homepage():
    if "guess" not in session:
        import random
        random_num = random.randint(1,100)
        print("*"*50)
        print("The session has been cleared.")
        print(f"Our random number is {random_num}")
        print("*"*50)
        session['random_num'] = random_num
    else:
        goal_num = int(session['random_num'])
        guess_num = int(session['guess'])
        print(f"The value of our guess is:{guess_num}. The value of our goal number is {goal_num}")
        if guess_num == goal_num:
            print("*"*50)
            print("You're so totally correct!!")
            session['phrase']=f"{goal_num} was the number!"
            print(session['phrase'])
            session['color']=f"green"
            print("*"*50)
        elif guess_num < goal_num:
            print("*"*50)
            print("the number is too low")
            session['phrase']=f"Too low!"
            session['color']=f"red"
            print(session['phrase'])
            print("*"*50)
        elif guess_num > goal_num:
            print("*"*50)
            print("the number is too high")
            session['phrase']=f"Too high!"
            print(session['phrase'])
            session['color']=f"red"
            print("*"*50)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['guess']=request.form['guess']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_numbers():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)