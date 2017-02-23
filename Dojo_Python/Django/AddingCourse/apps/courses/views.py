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

def destroy(request, id):
    course = Course.objects.get(id=id)
    context = {
    'name': course.name,
    'description': course.description,
    'id':course.id
    }
    # course.delete()
    return render(request,'courses/destroy.html', context)
    # return redirect('/')

def delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')

def comments(request, id):
    course = Course.objects.get(id=id)
    context = {
    'name': course.name,
    'description': course.description,
    'id':course.id,
    'comments': Comment.objects.filter(course=course)
    }
    return render(request, 'courses/comments.html', context)

def addcomment(request, id):
    course = Course.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], course=course)

    print id
    return redirect('/comments/{}'.format(id))
