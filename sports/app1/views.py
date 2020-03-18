from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from datetime import date


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year -((today.month, today.day) <(birth_date.month, birth_date.day))
    return age


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.profile.address = request.POST.get('address')
        user.profile.phone_no = request.POST.get('phone')
        user.profile.gender = request.POST.get('gender')
        year = int(request.POST.get('year'))
        month = int(request.POST.get('month'))
        day = int(request.POST.get('day'))
        user.profile.age = calculate_age(date(year, month, day))
        user.save()
        return redirect(request, 'app1/home.html')
    return render(request, 'app1/signup.html')


def login(request):
    if request.method == "POST":
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user, password=password)
        if user is not None:
            return redirect('app1/home.html')
        else:
            return redirect('app1/login.html')
    else:
        return render(request, 'app1/login.html')


def booking(request, game_id):
    game = Coaching.objects.get(pk=game_id)
    template = 'app1/bookings.html'
    context = {'game': game}
    return render(request, template, context)


def ad(request):
    template = 'app1/advertisement.html'
    ad = request.POST.get('advertisement ')
    return render(request, template)


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.profile.user)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.profile.user)

    context = {'u_form': u_form, 'p_form': p_form}
    template = 'app1/profile.html'
    return render(request, template, context)


def home(request):
    template = 'app1/home.html'
    return render(request, template)

