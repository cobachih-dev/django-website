from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CandidateForm

def index(request):
    if request.method == 'POST':
        print('Smn jala')
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'index.html')