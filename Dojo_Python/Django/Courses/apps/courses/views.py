from django.shortcuts import render, redirect
from .models import Course, Comment
# Create your views here.
def index(request):
    context = {
    'courses': Course.objects.all(),
    }
    return render(request, 'courses/index.html', context)

def course(request):

    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')
