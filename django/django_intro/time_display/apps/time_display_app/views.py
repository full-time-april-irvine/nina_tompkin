from django.shortcuts import render, HttpResponse
from time import localtime, strftime
from datetime import datetime

def display_time(request):
    context = {
        "time":strftime("%b %d %Y %I:%M %p",localtime())
    }
    return render(request,'time_display_app/index.html',context)
