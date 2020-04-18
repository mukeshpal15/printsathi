from django.core.paginator import *
from django.shortcuts import render, redirect
from django.conf import  settings
from django.urls import path
from printapp.models import *
from django.conf import  settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.contrib.auth import logout
from django.core.mail import EmailMessage

def CheckUserSession(request):
	e=request.session['user_email']
	if UserData.objects.filter(User_Email=e).get():
		return 1
	else:
		return 0
def GetDesignImageCount(request):
	obj=PropertyDesignData.objects.all()
	count=0
	lt=[]
	for x in obj:
		lt.append(x.Product_ID)
	lt1=lt
	lt=[]
	