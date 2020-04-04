from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    game_name = models.CharField(max_length=100)
    turf = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.game_name} '


class Coaching(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    time = models.DurationField()
    age = models.IntegerField(default=0)
    days_a_week = models.IntegerField(default=1)
    coach = models.CharField(max_length=250)
    turf = models.IntegerField(default=1)
    fees = models.FloatField(default=300)

    def __str__(self):
        return f'{self.game.game_name} Coaching'


class UserCoaching(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    SPAN = [('ONE MONTH', '1 month'), ('THREE MONTHS', '3 months'), ('SIX MONTHS', '6 months'), ('ONE YEAR', '1 year')]
    coaching_span = models.CharField(max_length=15, choices=SPAN, default='ONE MONTH')
    GENDER = [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')]
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE')
    enrolled_for = models.ForeignKey(Coaching, on_delete=models.CASCADE)


class Booking(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False)
    time = models.DurationField()
    price = models.FloatField(default=300)
    team_present = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.game}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    GENDER = [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')]
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE')
    classes = models.ManyToManyField(UserCoaching)
    bookings = models.ManyToManyField(Booking)
    address = models.TextField(max_length=500)
    phone_no = models.CharField(max_length=10)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'


class Team(models.Model):
    team_members = models.ManyToManyField(Profile)
    team_leader = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='team-leader+')
    booking = models.ManyToManyField(Booking)
