from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
     return render(request, 'account/index.html')