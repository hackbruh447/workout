from django.shortcuts import render
from django.http import HttpResponse



import os
import google.generativeai as genai



# Create your views here.

def homepage(request):
    return render(request, "diet/homepage.html")

def settings(request):
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


