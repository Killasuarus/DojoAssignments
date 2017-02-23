from django.shortcuts import render, HttpResponse, redirect
import random
import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    # create 'gold' variable
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'activites' not in request.session:
        request.session['activities']=[]
    return render(request, 'GoldGame\index.html')


def process_money(request):
    # set up values for buildings
    buildings={
    'farm': random.randint(10,20),
    'cave': random.randint(5,10),
    'house': random.randint(2,5),
    'casino': random.randint(-50,50)
    }
    place = request.POST['building']
    request.session['gold']+=buildings[place]

    request.session['activities']=place
    # create an activites message
        # log that messsage into index
    if buildings[place] > 0:
        messages.success(request, 'You went to the {} and won {} gold! ({})'.format(request.session['activities'],buildings[place], datetime.datetime.now()))
    else:
        messages.error(request, 'You went to the casino and lost {} gold.... ouch ({})'.format(buildings[place], datetime.datetime.now()))
    #print session['gold']
    print buildings[place]
    print request.session['activities']
    return redirect('/')
