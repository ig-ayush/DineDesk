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

def login_form(request):

    adminEmail = "acharyaayush1510@gmail.com";
    adminPassword = "developer"

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        if email == adminEmail and password == adminPassword:
            return redirect('/admin-dashboard')
        
        try:
            user_obj = User.objects.get(email=email)

            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user:
            login(request, user)

            next_url = request.GET.get("next")
            messages.success(request, "Login to account")
            return redirect(next_url if next_url else "/profile/")
        
        messages.error(request, "Invalid email or password")
        return redirect('/login')

    return render(request, 'login.html')

def signup(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("/signup-account")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username alredy exits")
            return redirect("/signup-account")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("/signup-account")
        
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("/login")

    return render(request, 'signup.html')

def logout_account(request):
    logout(request)
    return redirect('/login')

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')