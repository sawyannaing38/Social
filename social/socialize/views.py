from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .models import User, Post, Comment, Reactor
from django.db import IntegrityError
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "socialize/index.html")

# For Registering
def register(request):
    
    # For get method
    if request.method == "GET":
        return render(request, "socialize/register.html", {
            "message" : None
        })
    
    # For post method

    # Getting usrname, password and confirmation
    username = request.POST.get("username")
    password = request.POST.get("password")
    confirmation = request.POST.get("confirmation")

    if not username:
        return render(request, "socialize/register.html", {
            "message" : "Missing username"
        })
    
    if not password:
        return render(request, "socialize/register.html", {
            "message" : "Missing Password"
        })
    
    if not confirmation:
        return render(request, "socialize/register.html", {
            "message" : "Missing Confiramtion Password"
        })
    
    if password != confirmation:
        return render(request, "socialize/register.html", {
            "message" : "Passwords do not match"
        })
    
    # Try to create a user
    try:
        user = User.objects.create_user(username=username, password=password)

        # Saving user in model
        user.save()
    
    except IntegrityError:
        return render(request, "socialize/register.html", {
            "message" : "Username already taken"
        })
    
    else:
        # Logging in user
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

# For Loggin in
def login_view(request):
    
    # For get method
    if request.method == "GET":
        return render(request, "socialize/login.html", {
            "message" : None
        })
    
    # For post method
    # Getting username and password
    username = request.POST.get("username")
    password = request.POST.get("password")

    if not username:
        return render(request, "socialize/login.html", {
            "message" : "Missing Username"
        })
    
    if not password:
        return render(request, "socialize/login.html", {
            "message" : "Missing Password"
        })
    
    # Checking user
    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "socialize/login.html", {
            "message" : "Invalid Usrename or Password"
        })
    
# For Loggin out
def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse("login"))