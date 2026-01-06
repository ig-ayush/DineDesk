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
