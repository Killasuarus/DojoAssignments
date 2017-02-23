from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):

    return render(request, 'surveyform\index.html')

def users(request):
    if 'counter' not in request.session:
        request.session['counter']=1
    return render(request, 'surveyform\users.html')

def process(request):
    if 'counter' not in request.session:
        request.session['counter']=1
    else:
        request.session['counter']+=1
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comments']=request.POST['comments']
    return redirect('/users')
