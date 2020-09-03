from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CandidateForm

def index(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'website/home.html')