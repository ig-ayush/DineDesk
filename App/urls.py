from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile/', views.profile_view),
    path('login/', views.login_form),
    path('signup-account/', views.signup),
    path('logout-account', views.logout_account),
    path('admin-dashboard', views.admin_dashboard),
    path('add-restaurant', views.open_addRes),
    path('admin-restaurant', views.show_restaurant)
]