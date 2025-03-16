from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import User

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

def get_user_data(request):
    # Fetch users sorted by points (descending)
    users = User.objects.all().order_by('-points')
    
    # Create two separate lists: one for points and one for usernames
    points = [user.points for user in users]
    usernames = [user.username for user in users]
    
    # Return the data as a JSON response
    return JsonResponse({'points': points, 'usernames': usernames})

def homepage(request):

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
            user = request.user
            user.user = username
            user.goal = goal
            user.type = type
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


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "mail/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "diet/login.html")

def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "mail/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "diet/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("homepage"))
    else:
        return render(request, "diet/register.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))