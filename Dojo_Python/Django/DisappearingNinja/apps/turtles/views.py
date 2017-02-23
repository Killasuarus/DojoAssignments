from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'turtles/index.html')

def ninjas(request, color):
    if color == 'blue':
        context = {
        'tmnt': 'leonardo.jpg'
        }
    elif color == 'orange':
        context = {
        'tmnt': 'michelangelo.jpg'
        }
    elif color == 'red':
        context = {
        'tmnt': 'raphael.jpg'
        }
    elif color == 'purple':
        context = {
        'tmnt': 'donatello.jpg'
        }
    else:
        context = {
        'tmnt': 'notapril.jpg'
        }
    return render(request, 'turtles/ninjas.html', context)

def allninjas(request):
    context = {
    'tmnt': 'tmnt.png'
    }
    return render(request, 'turtles/ninjas.html', context)
