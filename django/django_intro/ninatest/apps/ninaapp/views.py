from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def new(request):
    return HttpResponse("new page from the first app")