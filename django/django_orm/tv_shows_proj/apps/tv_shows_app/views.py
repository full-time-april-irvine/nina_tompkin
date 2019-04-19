from django.shortcuts import render, redirect
from .models import Shows

def index(request):
    context = {
        "all_shows":Shows.objects.pull_all_shows()
    }
    return render(request, "tv_shows_app/index.html",context)

def new(request):
    
    return render(request, "tv_shows_app/new.html")

def create(request):
    #Create a new record in our database based on supplied form data.
    #Return the show id for the process of routing to its unique page.
    show_id = Shows.objects.easy_create(request.POST)
    return redirect(f"/shows/{show_id}")

def show(request, show_id):
    this_show = Shows.objects.get_this_show(show_id)
    context = {
        "this_show":this_show
    }
    return render(request, "tv_shows_app/show.html",context)

def edit(request, show_id):
    this_show = Shows.objects.get_this_show(show_id)
    context = {
        "this_show":this_show
    }
    return render(request, "tv_shows_app/edit.html",context)

def update(request, show_id):
    this_show = Shows.objects.update_this_show(show_id, request.POST)
    show_id = this_show.id
    return redirect(f"/shows/{show_id}")

def destroy(request, show_id):
    this_show = Shows.objects.get(id=show_id)
    this_show.delete()
    return redirect("/shows/")