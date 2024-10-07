from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
# Create your views here.


def trends(request):
    return render(request, 'trends.html')

def login(request):
    return render(request, 'login.html')
