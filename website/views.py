from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CandidateForm
from .models import Olympian

def index(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()

    context={
        "olympians": Olympian.objects.all().order_by("-participations","id")
    }
    # k=1
    for olympian in context["olympians"]:
        """ print(str(k)+".- "+str(olympian.id)+" - "+ olympian.full_name)
        k+=1 """
        olympian.languages=olympian.languages.split(", ")
        olympian.picture=olympian.picture.split("id=")
        olympian.picture=olympian.picture[1]

    # https://drive.google.com/u/0/open?usp=forms_web&id=1LBfYX85sorZ4hijASpMytW96OWvFavlV
    return render(request, 'website/home.html', context=context)