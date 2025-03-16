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
            user = User(name = username, goal = goal, type = type )
            user.save()

            return HttpResponseRedirect(reverse('homepage'))
       
        except:
            return render(request, "diet/settings.html", {
                    "invalid":"Please enter correct input"})

    return render(request, "diet/settings.html")


def ai(request):
    
    genai.configure(api_key="AIzaSyA86DMyWmRBxyWXgVJZOtWBGQCcSSBIpJQ")  # Replace with your actual API key

    model = genai.GenerativeModel("gemini-1.5-flash")  # Correct model initialization

    prompt = (
        "Generate 5 unique daily fitness challenges in JSON format. "
        "Each challenge should be an object with keys: 'title' (a short string), "
        "'description' (a brief explanation), and 'points' (an integer between 3 and 15 "
        "representing difficulty). The challenges should relate to calorie tracking, "
        "maintaining or creating a calorie deficit, or overall fitness. Return only the JSON array."
    )
    
    response = model.generate_content(prompt)
    print(response.text)
    
    try:
        # Parse the response from AI into a Python list.
        challenges = json.loads(response.text)
    except Exception as e:
        # Fallback to a static list if AI fails.
        challenges = [
            {"title": "10,000 Steps", "description": "Walk 10,000 steps today to boost your calorie burn.", "points": 5},
            {"title": "No Sugar Day", "description": "Avoid added sugars for a day to support your calorie deficit.", "points": 7},
            {"title": "High Protein Meal", "description": "Prepare a high-protein meal to aid muscle recovery.", "points": 10},
            {"title": "30 Minute Cardio", "description": "Do 30 minutes of cardio to improve endurance.", "points": 8},
            {"title": "Healthy Breakfast", "description": "Start your day with a balanced, nutritious breakfast.", "points": 4},
        ]
    
    return render(request, "diet/ai.html", {"challenges": challenges})
