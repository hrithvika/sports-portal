from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from datetime import date
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse


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
        return redirect('/home/')
    return render(request, 'app1/signup.html')


def login(request):
    if request.method == "POST":
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user, password=password)
        if user is not None:
            return redirect('/home/')
        else:
            messages.error(request, f'Invalid login credentials!')
            return redirect('/login/')
    else:
        return render(request, 'app1/login.html')


def booking(request):
    game = Game.objects.all()
    template = 'app1/bookings.html'
    context = {'games': game}
    return render(request, template, context)


def book_game(request, game_id):
    booked_game = Game.objects.get(id=game_id)
    teams = Team.objects.filter(booking__games=booked_game)
    profiles = Profile.objects.all()
    template = 'app1/game.html'
    members = None
    if request.method == 'POST':
        if 'join' in request.POST:
            profile = Profile.objects.get(user=request.user)
            team_id = request.POST.get("join-team")
            team = Team.objects.get(id=team_id)
            join_team = team.booking
            profile.bookings.add(join_team)
            profile.save()
        elif request.POST.get("create"):
            new_team = Team()
            team_leader = request.POST.get("name")
            team_leader = Profile.objects.get(username=team_leader)
            new_team.team_leader = team_leader
            new_team.team_name = request.POST.get("team-name")
            players = request.POST.getlist('team-players')
            for player in players:
                play = Profile.objects.get(id=player)
                new_team.team_members.add(play)
            members = new_team.team_members
            book = Booking()
            book.games = booked_game
            book.save()
            new_team.booking = book
            new_team.save()
    context = {'booked_game': booked_game, 'teams': teams, 'profiles': profiles, 'members': members}
    return render(request, template, context)


'''  user = request.user
    if request.method == "POST":
        enrolled_class = UserCoaching()
        enrolled_class.firstname = request.POST.get('fname')
        enrolled_class.lastname = request.POST.get('lname')
        age = request.POST.get('age')
        enrolled_class.gender = request.POST.get('gender')
        user.classes = enrolled_class
        user.save()
        return render(request, template, context)
    else:'''


def enroll_game(request, game_id):
    classes = Coaching.objects.filter(games__id=game_id).values('age')
    classes_list = list(classes)
    return JsonResponse(classes_list, safe=False)


class GameListView(ListView):
    model = Game
    template_name = 'app1/enroll.html'

    def get(self, request):
        games = Game.objects.all()
        classes = None
        if request.method == 'GET':
            for game in games:
                if request.GET.get('selected_game') == game.pk:
                    classes = Game.objects.get(pk=int(game.pk))
        return render(request, self.template_name, {'games': games, 'classes': classes})


def ad(request):
    template = 'app1/advertisement.html'
    ad = request.POST.get('advertisement ')
    return render(request, template)

'''
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
    return render(request, template, context)'''


def home(request):
    template = 'app1/home.html'
    return render(request, template)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    template = 'app1/profile.html'
    context = {'profile': profile}
    return render(request, template, context)
