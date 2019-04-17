from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request,"ninja_gold_app/index.html")

def randomNum(start,end):
    random_num = random.randint(start,end)
    return random_num

def process_money(request):
    if request.method =="POST":
        now = datetime.now().strftime('%Y/%m/%d %I:%M %p')
        if request.POST['building'] == "farm":
            new_gold = randomNum(10,20)
            request.session['gold_count'] += new_gold
            activity = {
                'content':f"Earned {new_gold} golds from the {request.POST['building']}! {now}",
                'css_class':"green-text"
            }
            request.session['activities'].insert(0,activity)
        elif request.POST['building'] =="cave":
            new_gold = randomNum(5,10)
            request.session['gold_count'] += new_gold
            activity = {
                'content':f"Earned {new_gold} golds from the {request.POST['building']}! {now}",
                'css_class':"green-text"
            }
            request.session['activities'].insert(0,activity)
        elif request.POST['building'] =="house":
            new_gold = randomNum(2,5)
            request.session['gold_count'] += new_gold
            activity = {
                'content':f"Earned {new_gold} golds from the {request.POST['building']}! {now}",
                'css_class':"green-text"
            }
            request.session['activities'].insert(0,activity)
        elif request.POST['building'] =="casino":
            new_gold = randomNum(-50,50)
            request.session['gold_count'] += new_gold
            if new_gold > 0:
                activity = {
                'content':f"Earned {new_gold} golds from the {request.POST['building']}! {now}",
                'css_class':"green-text"
                }
                request.session['activities'].insert(0,activity)
            else:
                activity = {
                'content':f"Entered a {request.POST['building']} and lost {new_gold} golds... Ouch. {now}",
                'css_class':"red-text"
                }
                request.session['activities'].insert(0,activity)
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")