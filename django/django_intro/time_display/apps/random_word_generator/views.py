from django.shortcuts import render, HttpResponse, redirecct

def display(request):
    return render(request,'random_word_generator/index.html')

def reset(request):
    pass
    return redirecct("/word_generator")
