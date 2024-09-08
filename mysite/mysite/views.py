from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        return render(request, 'mysite/index.html')
    else:
        return redirect('/account/login')