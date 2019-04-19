from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

def index(request):
    return render(request, "login_and_reg_app/index.html")

def create(request):
    errors = Users.objects.validate(request.POST)
    
    if errors:
        for error in errors:
            messages.error(request,error)
    return redirect("/")

    this_user = Users.objects(easy_create(request.POST))
    return redirect("/")

def login(request):
    this_user = Users.objects.filter(email=form["email"])
    request.session["user_id"] = this_user.id
    return render(request, "login_and_reg_app/success.html")

def show(request):
    return render(request, "login_and_reg_ap/success.html")

def logout(request):
    return redirect("/")