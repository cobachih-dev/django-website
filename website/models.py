from django.db import models
from django.forms import ModelForm

# Create your models here.
class Candidate(models.Model):
    full_name = models.CharField(max_length=255)
    matricula = models.CharField(max_length=30)
    school = models.IntegerField()
    group = models.IntegerField()
    email = models.EmailField(default='defaultemail@default.com')
    questions = models.TextField(max_length=255, blank=True)

class School(models.Model):
    image = models.ImageField(upload_to='schools')
    school_name = models.CharField(max_length=30)
    week_day = models.CharField(max_length=20)
    starting_time = models.TimeField(auto_now=False, auto_now_add=False)
    ending_time = models.TimeField(auto_now=False, auto_now_add=False)

class Olympian(models.Model):
    full_name = models.CharField(max_length=255)
    school = models.CharField(max_length=15)
    picture = models.URLField(default='')
    participations = models.CharField(max_length=50)
    achievements = models.CharField(max_length=500, default='')
    languages = models.CharField(max_length=255)
    career = models.CharField(max_length=200)