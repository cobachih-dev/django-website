from django.db import models
from django.forms import ModelForm

# Create your models here.
class Candidate(models.Model):
    full_name = models.CharField(max_length=255)
    matricula = models.CharField(max_length=30)
    school = models.IntegerField()
    group = models.IntegerField()
    description = models.TextField(max_length=1000, blank=True)
    questions = models.TextField(max_length=255, blank=True)

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'full_name',
            'matricula', 
            'school', 
            'group', 
            'description',
            'questions']
