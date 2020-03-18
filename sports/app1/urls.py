from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('ads/', views.ad, name='ad'),
    path('bookings/<int:game_id>/', views.booking, name='booking'),
    path('profile/', views.profile, name='profile'),
]
