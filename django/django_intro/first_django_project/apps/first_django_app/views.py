from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "name":"Nina",
        "favorite_color":"green",
        "pets":["Nicky","Stewart","Frodo"]
    }
    return render(request, "first_django_app/index.html", context)

def new(request):
    return HttpResponse("placeholder to display new form to create a new blog")

def create(request):
    return redirect("/")

def show(request,blog_num):
    return HttpResponse(f"Placeholder to display blog number: {blog_num}")

def edit(request,blog_num):
    return HttpResponse(f"Placeholder to edit blog {blog_num}")

def destroy(request,blog_num):
    return redirect("/")