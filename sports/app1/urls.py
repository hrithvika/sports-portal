from django.urls import path
from . import views
from .views import GameListView

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('ads/', views.ad, name='ad'),
    path('bookings/', views.booking, name='booking'),
    path('bookings/<int:game_id>/', views.book_game, name='book-game'),
    path('enroll/', GameListView.as_view(), name='enroll'),
    path('enroll/<int:game_id>/', views.enroll_game, name='enroll-class'),
    path('profile/', views.profile, name='profile'),
]
