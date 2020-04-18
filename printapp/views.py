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
from printapp.printutil import *

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
	return render(request,'adminlogin.html',{})
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
		dic={'data':PaperTypeData.objects.all(),
			'adata':ProductData.objects.filter(Product_Status="Active"),
			'ddata':ProductData.objects.filter(Product_Status="Deactive"),
			}
		return render(request, 'addproducts.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def saveproducts(request):
	if request.method=="POST":
		p="PR00"
		x=1
		pid=p+str(x)
		while ProductData.objects.filter(Product_ID=pid).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		if ProductData.objects.filter(Product_Name=request.POST.get('name')).exists():
			dic={'msg':"Product Already Exists",
			'data':PaperTypeData.objects.all(),
			'adata':ProductData.objects.filter(Product_Status="Active"),
			'ddata':ProductData.objects.filter(Product_Status="Deactive")}
			return render(request, 'addproducts.html',dic)
		else:
			obj=ProductData(
				Product_ID=pid,
				Product_Name=request.POST.get('name'),
				Product_Paper_Type=request.POST.get('ptype'),
				Product_Category=request.POST.get('category'),
				Product_Thickness=request.POST.get('thickness'),
				Product_Lamination=request.POST.get('lamination'),
				Product_Quantity=request.POST.get('quantity'),
				Product_Print_Sides=request.POST.get('printside'),
				Product_Color=request.POST.get('color'),
				Product_Size=request.POST.get('size'),
				Product_Status='Active',
				)
			obj.save()
			dic={'msg':"Saved Successfully",
			'data':PaperTypeData.objects.all(),
			'adata':ProductData.objects.filter(Product_Status="Active"),
			'ddata':ProductData.objects.filter(Product_Status="Deactive")}
			return render(request, 'addproducts.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def deleteproducts(request):
	if request.method=="POST":
		obj=ProductData.objects.filter(Product_ID=request.POST.get('delete')).delete()
		dic={'msg':"Deleted Successfully",
		'data':PaperTypeData.objects.all(),
		'adata':ProductData.objects.filter(Product_Status="Active"),
		'ddata':ProductData.objects.filter(Product_Status="Deactive")}
		return render(request, 'addproducts.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def deactiveproducts(request):
	if request.method=="POST":
		obj=ProductData.objects.filter(Product_ID=request.POST.get('delete')).update(Product_Status="Deactive")
		dic={'msg':"Deactivated Successfully",
		'data':PaperTypeData.objects.all(),
		'adata':ProductData.objects.filter(Product_Status="Active"),
		'ddata':ProductData.objects.filter(Product_Status="Deactive")}
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
<<<<<<< HEAD

@csrf_exempt
def saveuser(request):
	if request.method=="POST":
		u="U00"
		x=1
		uid=u+str(x)
		while UserData.objects.filter(User_Email=request.POST.get('email')).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		if UserData.objects.filter(User_Email=request.POST.get('Email'),User_Phone=request.POST.get('Phone Number')).exists():
			dic={'msg':"User Already Registered"}
			return render(request, 'userregistration.html',dic)
		else:
			otp=uuid.uuid5(uuid.NAMESPACE_DNS, request.POST.get('Email')+uid)
			password=str(otp)
			password=password.upper()[0:8]
			obj=UserData(
				User_ID=uid,
				User_First_Name=request.POST.get('First Name'),
				User_Last_Name=request.POST.get('Last Name'),
				User_Gender=request.POST.get('Gender'),
				User_Email=request.POST.get('Email'),
				User_Phone=request.POST.get('Phone Number'),
				User_Address=request.POST.get('Address'),
				User_City=request.POST.get('City'),
				User_State=request.POST.get('State'),
				User_Password=password
			)
			obj.save()
			msg = '''Hi there!
Your account has been Successfully created on Printsathi. Your account credentials are as below,
Email : '''+request.POST.get('Email')+'''
Password : '''+password+'''

Thanks & Regards,
Printsathi'''
			sub='Welcome to Printsathi'
			email = EmailMessage(sub, msg, to=[request.POST.get('Email')])
			email.send()
			dic={'msg':"Successfully Registered",
				'msg1':'You will get you account credentials on your mail soon.'}
			return render(request, 'userregistration.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def userlog(request):
	if request.method=='POST':
		check=1
		dic={}
		if UserData.objects.filter(User_Email=request.POST.get('email'),User_Password=request.POST.get('pass')).exists():
			request.session['user_email'] = request.POST.get('email')
			for x in UserData.objects.filter(User_Email=request.POST.get('email')):
				dic={'fname': x.User_First_Name,
					'lname': x.User_Last_Name,
					'email': x.User_Email,
					'phone': x.User_Phone,
					'address': x.User_Address,
					'city': x.User_City,
					'state': x.User_State,
					'session':CheckUserSession(request),
					'checksession':1}
			return render(request,'profile.html',dic)
		else:
			dic={'msg':'Incorrect Email or Password',}
			return render(request,'userlogin.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
@csrf_exempt
def changeuserpassword(request):
	if request.method=="POST":
		dic={}
		if UserData.objects.filter(User_Email=request.session['user_email'],User_Password=request.POST.get('opass')).exists():
			obj=UserData.objects.filter(User_Email=request.session['user_email'],User_Password=request.POST.get('opass'))
			obj.update(User_Password=request.POST.get('npass'))
			for x in obj:
				dic={'fname': x.User_First_Name,
				'lname': x.User_Last_Name,
				'email': x.User_Email,
				'phone': x.User_Phone,
				'address': x.User_Address,
				'city': x.User_City,
				'state': x.User_State,
				'session':CheckUserSession(request),
				'checksession':1
				}
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Password Changed Successfully'+b2
			dic.update({'alert':alert})
			msg = '''Hi there!
Your account's password has been changed,

New Password : '''+request.POST.get('npass')+'''

If this was not you report us now!

Thanks & Regards,
Printsathi'''
			sub='Alert! Your Password Has Been Changed'
			email = EmailMessage(sub, msg, to=[request.session['user_email']])
			email.send()
			return render(request,'profile.html',dic)
		else:
			obj=UserData.objects.filter(User_Email=request.session['user_email'])
			for x in obj:
				dic={'fname': x.User_First_Name,
				'lname': x.User_Last_Name,
				'email': x.User_Email,
				'phone': x.User_Phone,
				'address': x.User_Address,
				'city': x.User_City,
				'state': x.User_State,
				'session':CheckUserSession(request),
				'checksession':1
				}
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Incorrect Password'+b2
			dic.update({'alert':alert})
			return render(request,'profile.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def changeuserdetails(request):
	if request.method=="POST":
		dic={}
		obj=UserData.objects.filter(User_Email=request.session['user_email'])
		obj.update(
			User_Phone=request.POST.get('Phone'),
			User_Address=request.POST.get('Address'),
			User_City=request.POST.get('City'),
			User_State=request.POST.get('State')
			)
		for x in obj:
			dic={'fname': x.User_First_Name,
				'lname': x.User_Last_Name,
				'email': x.User_Email,
				'phone': x.User_Phone,
				'address': x.User_Address,
				'city': x.User_City,
				'state': x.User_State,
				'session':CheckUserSession(request),
				'checksession':1
			}
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Changes Saved Successfully'+b2
		dic.update({'alert':alert})
		return render(request,'profile.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
def myorders(request):
	return render(request, 'myorders.html',{})
def myordersdetails(request):
	return render(request, 'myordersdetails.html',{})
