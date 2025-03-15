from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, "diet/homepage.html")

def challenges(request):
    return render(request, "diet/challenges.html")