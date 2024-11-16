from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')