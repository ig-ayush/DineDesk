from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'address',
            'opening_time',
            'closing_time',
            'phone_number',
            'rating',
            'image',
            'description'
        ]