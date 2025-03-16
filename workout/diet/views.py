from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import userInfo

import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.views.decorators.csrf import csrf_exempt

import os
import google.generativeai as genai



# Create your views here.

def homepage(request):
    lst=[]
    users = userInfo.objects.all()
    
        
    return render(request, "diet/homepage.html",{
        
    })

@csrf_exempt
def settings(request):

    if request.method=="POST":
        username = request.POST["username"]
        goal = request.POST["goal"]
        description = request.POST["caloric_choice"]
        if((description)=="intake"):
            type = True
        else:
            type = False

        try:
            user = userInfo(name = username, goal = goal, type = type )
            user.save()

            return HttpResponseRedirect(reverse('homepage'))
       
        except:
            return render(request, "diet/settings.html", {
                    "invalid":"Please enter correct input"})

    return render(request, "diet/settings.html")


def ai(request):
    
    genai.configure(api_key="AIzaSyA86DMyWmRBxyWXgVJZOtWBGQCcSSBIpJQ")  # Replace with your actual API key

    model = genai.GenerativeModel("gemini-1.5-flash")  # Correct model initialization

    prompt = """List a few popular cookie recipes in JSON format.

    Use this JSON schema:

    Recipe = {'recipe_name': str, 'ingredients': list[str]}
    Return: list[Recipe]
    """

    response = model.generate_content(prompt)

    print(response.text)

    return render(request, "diet/ai.html")


