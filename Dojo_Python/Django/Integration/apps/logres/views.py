from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request, 'logres/index.html')

def registration(request):
    response_from_models = User.objects.register(request.POST)
    # check status from models
    if response_from_models['status']:
        # created a user, send to success page
        request.session['user_id'] = response_from_models['user'].id
        request.session['user_name'] = response_from_models['user'].first_name
        return redirect('users:success')
        pass
    else:
        for error in response_from_models['errors']:
            messages.error(request, error)
        return redirect('users:index')

def login(request):
    response_from_models = User.objects.login(request.POST)


    if response_from_models['status']:
        request.session['user_id'] = response_from_models['user'].id
        request.session['user_name'] = response_from_models['user'].first_name

        return redirect('users:success')
    else:
        messages.error(request, response_from_models['errors'])
        return redirect('users:index')


def success(request):
    if not 'user_id' in request.session:
        messages.error(request, 'Must be logged in to continue!')
        return redirect('users:index')
    return render(request, 'logres/success.html')

def logout(request):
    request.session.clear()

    return redirect('users:index')
