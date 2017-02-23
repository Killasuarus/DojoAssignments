from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] =1
    random_word = {
    'generate':get_random_string(length=14)
    }
    return render(request, 'ranwordgen\index.html', random_word)

def count(request):
    request.session['counter'] +=1
    return redirect('/')
