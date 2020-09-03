from django.contrib import admin
from .models import Candidate, School

# Register your models here.

admin.site.register(School)
admin.site.register(Candidate)