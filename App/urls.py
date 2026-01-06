from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('profile/', views.profile_view),
    path('login/', views.login_form),
    path('signup-account/', views.signup),
    path('logout-account', views.logout_account),
    path('admin-dashboard', views.admin_dashboard, name='admin-dashboard'),
    path('add-restaurant', views.add_restaurent, name='add-restaurant'),
    path('admin-restaurant', views.show_restaurant, name='admin-restaurant')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)