from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    date = {
    "current":datetime.datetime.now()
    }
    return render(request, 'timedisplay\index.html', date)


# Create your views here.
