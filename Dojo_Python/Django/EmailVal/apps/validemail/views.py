from django.shortcuts import render, redirect
from django.contrib import messages
from models import Email

# Create your views here.
def index(request):
    # modelResponse = Email.objects.add(request.POST)
    # if not modelResponse['status']:
    #     for error in modelResponse['errors']:
    #         message.error(request, error)

    return render(request, 'validemail/index.html')

def success(request):
    modelResponse = Email.objects.add_email(request.POST)
    if not modelResponse['status']:
        error = modelResponse['errors']
        messages.error(request, error)
        return redirect('/')
    else:
        context = {
        'emails': Email.objects.all()
        }
        return render(request, 'validemail/success.html', context)
