from django.db import models

class Restaurant(models.Model):

    name = models.CharField(max_length=100)
    address = models.TextField()

    opening_time = models.TimeField()
    closing_time = models.TimeField()

    phone_number = models.CharField(max_length=15)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    image =  models.ImageField(upload_to="restaurants/")
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Dish(models.Model):

    DISH_TYPE_CHOICES = [('veg', 'Veg'),('non-veg', 'Non-Veg')]

    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    ]

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='dishes/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dish_type = models.CharField(max_length=10, choices=DISH_TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
