from django.contrib.auth.models import User
from django.db import models


class Coaching(models.Model):
    game_name = models.CharField(max_length=100)
    time = models.DurationField()
    coach = models.CharField(max_length=250)
    turf = models.IntegerField(default=1)
    SPAN = [('ONE MONTH', '1 month'), ('THREE MONTHS', '3 months'), ('SIX MONTHS', '6 months'), ('ONE YEAR', '1 year')]
    coaching_span = models.CharField(max_length=15, choices=SPAN, default='ONE MONTH')
    fees = models.FloatField(default=300)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    GENDER = [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')]
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE')
    game = models.ManyToManyField(Coaching)
    address = models.TextField(max_length=500)
    phone_no = models.CharField(max_length=10)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


class Booking(models.Model):
    game = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=False)
    time = models.DurationField()
    price = models.FloatField(default=300)
    team_present = models.BooleanField(default=False)



