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
    path('admin-restaurant', views.show_restaurant, name='admin-restaurant'),
    path('edit-restaurant/<int:restaurant_id>', views.edit_restaurant, name='edit-restaurant'),
    path('admin-menu/<int:restaurant_id>', views.admin_menu, name='admin-menu'),
    path('add-dish/<int:restaurant_id>', views.add_dish, name='add-dish'),
    path('edit-dish/<int:dish_id>', views.edit_dish, name='edit-dish'),
    path('delete-restaurant/<int:restaurant_id>', views.delete_restaurant, name='delete-restaurant'),
    path('delete-dish/<int:dish_id>', views.delete_dish, name='delete-dish'),
    path('restaurant-menu/<int:restaurant_id>', views.restaurant_menu, name='restaurant-menu'),
    path('add-cart/<int:dish_id>', views.add_cart, name= 'add-cart'),
    path('user-cart', views.cart_view, name='user-cart'),
    path('user-cart/remove-item/<int:item_id>/', views.remove_item, name='remove-from-cart'),
    path('user-cart/clear', views.clear_cart, name= 'clear-cart')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)