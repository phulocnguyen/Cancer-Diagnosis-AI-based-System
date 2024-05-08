from django.shortcuts import render

# Create your views here.
def abstract(request):
    context={}
    return render(request, 'abstract.html', context)

def contact(request):
    context={}
    return render(request, 'contact.html', context)

def dashboard(request):
    context={}
    return render(request, 'dashboard.html', context)

def index(request):
    context={}
    return render(request, 'index.html', context)

def login(request):
    context={}
    return render(request, 'login.html', context)

def preview(request):
    context={}
    return render(request, 'preview.html', context)

def signup(request):
    context={}
    return render(request, 'signup.html', context)

def upload(request):
    context={}
    return render(request, 'upload.html', context)

