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
	try:
		e=request.session['user_email']
		if UserData.objects.filter(User_Email=e).exists():
			return 1
	except:
		return 0
def GetCount(pid):
	obj=ProductDesignData.objects.filter(Product_ID=pid)
	count=0
	for x in obj:
		count=count+1
	return str(count)

def GetDesignImageCount():
	obj=ProductDesignData.objects.all()
	count=0
	dic={}
	lt=[]
	pid=[]
	icount=[]
	for x in obj:
		pid.append(x.Product_ID)
		icount.append(GetCount(x.Product_ID))
	pid=list(set(pid))
	icount=list(set(icount))
	for (a,b) in zip(pid,icount):
		dic={'id':a,
			'count':b,
			}
		lt.append(dic)
	return lt