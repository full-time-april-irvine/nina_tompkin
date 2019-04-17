from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 0
        request.session['rando_word'] = "STARTERSTRING"
    print(f"Our current count is: {request.session['count']}")
    return render(request,"random_word_generator_app/index.html")

def process(request):
    if request.method =="GET":
        print("A GET request is being made to this route.")
    if request.method == "POST":
        random_word = get_random_string(length=14,allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        request.session['rando_word'] = random_word
        print(f"A POST request is being made to this route. Our random word is: {random_word}")
        return redirect("/")

def reset(request):
    request.session.clear()
    print(f"our current count is 0.")
    return redirect("/")