from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
# Create your views here.


def trends(request):
    return render(request, 'trends.html')

def login(request):
    return render(request, 'login.html')

def landing_page(request):
    return render(request, 'landing_page.html')

def calculate_score(request):
    return render(request, 'score.html') 
