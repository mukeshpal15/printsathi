from django.shortcuts import render
from django.urls import path
from .models import *
from django.conf import  settings

# Create your views here.
def index(request):
	return render(request, 'index.html', {})
