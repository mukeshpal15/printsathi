from django.shortcuts import render
from django.urls import path
from printapp.models import *
from django.conf import  settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

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

	
@csrf_exempt
def admindash(request):
	if request.method=="POST":
		e=request.POST.get('email')
		p=request.POST.get('pass')
		if e=="admin@printsathi.com" and p=="1234":
			return render(request, 'admindash.html',{})
		else:
			return HttpResponse('<h1>Error</h1>')
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
@csrf_exempt
def backtoadmindash(request):
	if request.method=="POST":
		return render(request, 'admindash.html',{})
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
@csrf_exempt
def addproducts(request):
	if request.method=="POST":
		dic={'data':PaperTypeData.objects.all()}
		return render(request, 'addproducts.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def addpapertype(request):
	if request.method=="POST":
		dic={'data':PaperTypeData.objects.all()}
		return render(request, 'addpapertype.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
@csrf_exempt
def savepapertype(request):
	if request.method=="POST":
		n=request.POST.get('name')
		p="PA00"
		x=1
		pid=p+str(x)
		while PaperTypeData.objects.filter(Paper_ID=pid).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		if PaperTypeData.objects.filter(Paper_Name=n).exists():
			dic={'msg':"Paper Type Already Exists",
			'data':PaperTypeData.objects.all()}
			return render(request, 'addpapertype.html',dic)
		else:
			obj=PaperTypeData(
				Paper_ID=pid,
				Paper_Name=n
				)
			obj.save()
			dic={'msg':"Saved Successfully",
				'data':PaperTypeData.objects.all()}
			return render(request, 'addpapertype.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def DeletePaperType(request):
	if request.method=="POST":
		n=request.POST.get('name')
		obj=PaperTypeData.objects.filter(Paper_ID=request.POST.get('delete')).delete()
		dic={'msg':"Deleted Successfully",
			'data':PaperTypeData.objects.all()}
		return render(request, 'addpapertype.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
def myorders(request):
	return render(request, 'myorders.html',{})
def myordersdetails(request):
	return render(request, 'myordersdetails.html',{})
