from django.shortcuts import render

def index(request):
    return render(request, 'core/base.html')

def patients(request):
    pass

def treatments(request):
    pass