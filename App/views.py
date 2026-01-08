from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, Dish


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
            user_obj = User.objects.get(email=email)

            user = authenticate(request, username=user_obj.username, password=password)
            login(request, user)
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

def add_restaurent(request):

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        phone_number = request.POST.get('phone_number')
        rating = request.POST.get('rating')
        description = request.POST.get('description')

        image = request.FILES.get('image') 

        Restaurant.objects.create(
            name=name,
            address=address,
            opening_time=opening_time,
            closing_time=closing_time,
            phone_number=phone_number,
            rating=rating,
            image=image,
            description=description
        )

        restaurants = Restaurant.objects.all()
        return render(request, 'admin/admin_restaurants.html', {'restaurants' : restaurants})

    return render(request, 'admin/add_restaurant.html') 

def show_restaurant(request):
    
    restaurants = Restaurant.objects.all()
    return render(request, 'admin/admin_restaurants.html', {'restaurants' : restaurants})


def edit_restaurant(request, restaurant_id):

    restaurantList = Restaurant.objects.get(id = restaurant_id)
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        opening_time = request.POST.get('opening_time')
        closing_time = request.POST.get('closing_time')
        phone_number = request.POST.get('phone_number')
        rating = request.POST.get('rating')
        description = request.POST.get('description')
        image = request.FILES.get('image') 

        restaurantList.name = name
        restaurantList.address = address
        restaurantList.opening_time = opening_time
        restaurantList.closing_time = closing_time
        restaurantList.phone_number = phone_number
        restaurantList.rating = rating
        restaurantList.description = description
        restaurantList.image = image

        restaurantList.save()

        restaurants = Restaurant.objects.all()
        return render(request, 'admin/admin_restaurants.html', {'restaurants' : restaurants})
    
    return render(request, 'admin/edit_restaurant.html', {'restaurantList': restaurantList})
        

def admin_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id= restaurant_id)
    dishes = restaurant.dishes.all()
    return render(request, 'admin/manage_menu.html', {'restaurant': restaurant,'dishes': dishes})

def add_dish(request, restaurant_id):
    
    restaurant = Restaurant.objects.get(id= restaurant_id)
    if request.method == "POST":

        Dish.objects.create(
            restaurant=restaurant,
            name=request.POST.get('name'),
            image=request.FILES.get('image'),
            price=request.POST.get('price'),
            description=request.POST.get('description'),
            dish_type=request.POST.get('dish_type'),
            category=request.POST.get('category'),
        )

        return redirect('admin-menu', restaurant_id = restaurant.id)
    return render(request, 'admin/add_dish.html', {'restaurant' : restaurant})

def edit_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    restaurant = dish.restaurant

    if request.method == 'POST':
        dish.name = request.POST.get('name')
        dish.price = request.POST.get('price')
        dish.description = request.POST.get('description')
        dish.dish_type = request.POST.get('dish_type')
        dish.category = request.POST.get('category')

        if request.FILES.get('image'):
            dish.image = request.FILES.get('image')

        dish.save()

        return redirect('admin-menu', restaurant_id=restaurant.id)

    return render(request, 'admin/edit_dish.html', {
        'dishList': dish
    })

def delete_restaurant(request, restaurant_id):

    restaurant = get_object_or_404(Restaurant, id= restaurant_id)
    restaurant.delete()

    return redirect('admin-restaurant')

def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    restaurant_id = dish.restaurant.id

    dish.delete()

    return redirect('admin-menu', restaurant_id=restaurant_id)

