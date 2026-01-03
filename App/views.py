from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

def login(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)

            next_url = request.GET.get("next")
            return redirect(next_url if next_url else "profile")
        
        HttpResponse("Invalid username or password")
        return redirect('/login')

    return render(request, 'login.html')