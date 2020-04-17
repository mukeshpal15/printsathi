from django.shortcuts import render
from django.urls import path
from .models import *
from django.conf import  settings

# Create your views here.
def index(request):
	return render(request, 'index.html', {})
def aboutus(request):
	return render(request, 'about-us.html',{})
def allproducts(request):
	return render(request, 'allproducts.html',{})
def category(request):
	return render(request, 'category.html',{})
def cms(request):
	return render(request, 'cms.html',{})
def coomingsoon(request):
	return render(request, 'cooming-soon.html',{})
def howitworks(request):
	return render(request, 'howitworks.html',{})
def pricing(request):
	return render(request, 'pricing.html',{})
def productdetails(request):
	return render(request, 'productdetails.html',{})
def adminlogin(request):
	return render(request, 'adminlogin.html',{})
def addproducts(request):
	return render(request, 'addproducts.html',{})
def userlogin(request):
	return render(request, 'userlogin.html',{})
def userregistration(request):
	return render(request, 'userregistration.html',{})