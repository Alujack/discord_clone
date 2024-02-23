from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    works = ['1. need to define database', '2. System design',
             '3. i hope you can write html from ']
    context = {
        'works': works
    }
    return render(request, "base/home.html", context)
