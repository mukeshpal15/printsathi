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
from printapp.form import *

def index(request):
	dic={'session':CheckUserSession(request),
			'checksession':1,'detail':GetProductDetail()}
	return render(request, 'index.html', dic)		
def aboutus(request):
	dic={'session':CheckUserSession(request),
			'checksession':1}
	return render(request, 'about-us.html',dic)
def allproducts(request):
	dic={'session':CheckUserSession(request),
			'checksession':1}
	return render(request, 'allproducts.html',dic)
def category(request):
	dic={'session':CheckUserSession(request),
			'checksession':1}
	return render(request, 'category.html',dic)
def cms(request):
	dic={'session':CheckUserSession(request),
			'checksession':1}
	return render(request, 'cms.html',dic)
def coomingsoon(request):
	return render(request, 'cooming-soon.html',{})
def howitworks(request):
	return render(request, 'howitworks.html',{})
def pricing(request):
	return render(request, 'pricing.html',{})
def productdetails(request):
	detail=request.GET.get('cname')
	dic1=GetAgainProductDetail(detail)
	dic1.update({'session':CheckUserSession(request),
				'checksession':1})
	return render(request, 'productdetails.html',dic1)
def adminlogin(request):
	return render(request,'adminlogin.html',{})
def addproducts(request):
	return render(request, 'addproducts.html',{})
def userlogin(request):
	dic={'session':CheckUserSession(request),
		'checksession':1}
	return render(request, 'userlogin.html',dic)
def userregistration(request):
	dic={'session':CheckUserSession(request),
		'checksession':1}
	return render(request, 'userregistration.html',dic)
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
				Product_Price=request.POST.get('price'),
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
		obj2=ProductDesignData.objects.filter(Product_ID=request.POST.get('delete')).delete()
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

@csrf_exempt
def saveuser(request):
	if request.method=="POST":
		u="U00"
		x=1
		uid=u+str(x)
		while UserData.objects.filter(User_ID=uid).exists():
			x=x+1
			uid=u+str(x)
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
				'msg1':'You will get you account credentials on your mail soon.',
				'session':CheckUserSession(request),
				'checksession':1}
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
def myuseraccount(request):
	try:
		if UserData.objects.filter(User_Email=request.session['user_email']).exists():
			dic={}
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
			return render(request,'profile.html',dic)	
	except:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
@csrf_exempt
def adddesigns(request):
	if request.method=="POST":
		dic={'prod':ProductData.objects.filter(Product_Status='Active'),
			'data':GetDesignImageCount()}
		return render(request, 'adddesigns.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def savedesigns(request):
	if request.method=="POST":
		form=ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			m=form.cleaned_data['image']
			u="D00"
			x=1
			uid=u+str(x)
			while ResellerData.objects.filter(Reseller_ID=uid).exists():
				x=x+1
				uid=u+str(x)
			x=int(x)
			obj=ProductDesignData(
				Design_ID=uid,
				Product_ID=request.POST.get('Product'),
				Design_Image=m
				)
			obj.save()
			dic={'prod':ProductData.objects.filter(Product_Status='Active'),
				'msg':'Saved',
				'data':GetDesignImageCount()}
			return render(request, 'adddesigns.html',dic)
		else:
			return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
@csrf_exempt
def logout(request):
	try:	
		del request.session['user_email']
		request.session.flush()
		dic={'session':CheckUserSession(request),
			'checksession':1}
		return render(request, 'index.html',dic)
	except:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

def resellerregistration(request):
	dic={'session':CheckUserSession(request),
		'checksession':1}
	return render(request,'resellerregistration.html',dic)
@csrf_exempt
def savereseller(request):
	if request.method=="POST":
		u="R00"
		x=1
		uid=u+str(x)
		while ResellerData.objects.filter(Reseller_ID=uid).exists():
			x=x+1
			uid=u+str(x)
		x=int(x)
		if ResellerData.objects.filter(Reseller_Email=request.POST.get('Email'), Reseller_Phone=request.POST.get('Phone Number')):
			dic={'msg':"Reseller Already Registered"}
			return render(request, 'resellerregistration.html',dic)
		else:
			otp=uuid.uuid5(uuid.NAMESPACE_DNS, request.POST.get('Email')+uid)
			password=str(otp)
			password=password.upper()[0:8]
			obj=ResellerData(Reseller_ID=uid,
							Reseller_First_Name=request.POST.get('First Name'),
							Reseller_Last_Name=request.POST.get('Last Name'),
							Reseller_Gender=request.POST.get('Gender'),
							Reseller_Email=request.POST.get('Email'),
							Reseller_Phone=request.POST.get('Phone Number'),
							Reseller_Address=request.POST.get('Address'),
							Reseller_City=request.POST.get('City'),
							Reseller_State=request.POST.get('State'),
							Reseller_GSTIN=request.POST.get('GSTIN'),
							Reseller_PAN=request.POST.get('PAN'),
							Reseller_Password=password,
							Reseller_Status='Deactive',
							Adhaar=request.FILES['adhaar'],
							Profile=request.FILES['profile']	
							)
			obj.save()
			msg = '''Hi there!
Your Reseller's Account has been successfully created. We are reviewing your details.

Till then wait for our response.

Thanks & Regards,
Printsathi'''
			sub='Welcome to Printsathi'
			email = EmailMessage(sub, msg, to=[request.POST.get('Email')])
			email.send()
			dic={'msg':"Reseller Registered Successfully",
				'msg1':"Your password has been sent to your email."}
			return render(request, 'resellerregistration.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
def resellerlogin(request):
	dic={'session':CheckUserSession(request),
		'checksession':1}
	return render(request, 'resellerlogin.html',dic)

@csrf_exempt
def resellerlog(request):
	if request.method=='POST':
		d='Deactive'
		check=1
		dic={}
		if ResellerData.objects.filter(Reseller_Email=request.POST.get('email'),Reseller_Password=request.POST.get('pass')):
			request.session['re_email'] = request.POST.get('email')
			if ResellerData.objects.filter(Reseller_Status=d).exists():
				dic={'msg':'Your account is deactivated. Please wait admin response',}
				return render(request,'resellerlogin.html',dic)
			else:
				for x in ResellerData.objects.filter(Reseller_Email=request.session['re_email']):
					dic={'fname': x.Reseller_First_Name,
						'lname': x.Reseller_Last_Name,
						'email': x.Reseller_Email,
						'phone': x.Reseller_Phone,
						'address': x.Reseller_Address,
						'city': x.Reseller_City,
						'state': x.Reseller_State,
						'session':CheckUserSession(request),
						'checksession':1}
				return render(request,'resellerprofile.html',dic)
		else:
			dic={'msg':'Incorrect Email or Password',}
			return render(request,'resellerlogin.html',dic)


@csrf_exempt
def resellerdata(request):
	if request.method=="POST":
		dic={'adata':ResellerData.objects.filter(Reseller_Status="Active"),
			'ddata':ResellerData.objects.filter(Reseller_Status="Deactive")}
		return render(request,'resellerdata.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def changeresellerdetails(request):
	if request.method=="POST":
		dic={}
		obj=ResellerData.objects.filter(Reseller_Email=request.session['re_email'])
		obj.update(
			Reseller_Phone=request.POST.get('Phone'),
			Reseller_Address=request.POST.get('Address'),
			Reseller_City=request.POST.get('City'),
			Reseller_Status=request.POST.get('State')
			)
		for x in obj:
			dic={'fname': x.Reseller_First_Name,
				'lname': x.Reseller_Last_Name,
				'email': x.Reseller_Email,
				'phone': x.Reseller_Phone,
				'address': x.Reseller_Address,
				'city': x.Reseller_City,
				'state': x.Reseller_Status,
				'session':CheckUserSession(request),
				'checksession':1
			}
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Changes Saved Successfully'+b2
		dic.update({'alert':alert})
		return render(request,'resellerprofile.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
@csrf_exempt
def changeresellerpassword(request):
	if request.method=="POST":
		dic={}
		n=request.session['re_email']
		if ResellerData.objects.filter(Reseller_Email=request.session['re_email'],Reseller_Password=request.POST.get('opass')).exists():
			obj=ResellerData.objects.filter(Reseller_Email=request.session['re_email'],Reseller_Password=request.POST.get('opass'))
			obj.update(Reseller_Password=request.POST.get('npass'))
			for x in obj:
				dic={'fname': x.Reseller_First_Name,
				'lname': x.Reseller_Last_Name,
				'email': x.Reseller_Email,
				'phone': x.Reseller_Phone,
				'address': x.Reseller_Address,
				'city': x.Reseller_City,
				'state': x.Reseller_State,
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
			email = EmailMessage(sub, msg, to=[n])
			email.send()
			return render(request,'resellerprofile.html',dic)
		else:
			obj=ResellerData.objects.filter(Reseller_Email=request.session['re_email'])
			for x in obj:
				dic={'fname': x.Reseller_First_Name,
				'lname': x.Reseller_Last_Name,
				'email': x.Reseller_Email,
				'phone': x.Reseller_Phone,
				'address': x.Reseller_Address,
				'city': x.Reseller_City,
				'state': x.Reseller_State,
				'session':CheckUserSession(request),
				'checksession':1
				}
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Incorrect Password'+b2
			dic.update({'alert':alert})
			return render(request,'resellerprofile.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

def reselleractive(request):
	if request.method=="POST":
		obj=ResellerData.objects.filter(Reseller_ID=request.POST.get('id'))
		obj.update(Reseller_Status='Active')
		e=''
		p=''
		for x in obj:
			e=x.Reseller_Email
			p=x.Reseller_Password
			break
		msg = '''Hi there!
Your Reseller Account has been activated successfully,

Password : '''+p+'''

Thanks & Regards,
Printsathi'''
		sub='Congratulations! Reseller Account Activated Successfully'
		email = EmailMessage(sub, msg, to=[e])
		email.send()
		dic={'adata':ResellerData.objects.filter(Reseller_Status="Active"),
			'ddata':ResellerData.objects.filter(Reseller_Status="Deactive")}
		return render(request,'resellerdata.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def resellerdeactive(request):
	if request.method=="POST":
		obj=ResellerData.objects.filter(Reseller_ID=request.POST.get('id'))
		obj.update(Reseller_Status="Deactive")
		dic={'adata':ResellerData.objects.filter(Reseller_Status="Active"),
			'ddata':ResellerData.objects.filter(Reseller_Status="Deactive")}
		return render(request,'resellerdata.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def opencategory(request):
	cname=request.GET.get('cname')
	dic={'data':GetProductDetailByCategory(cname)}
	if cname=='Business Cards':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/Visiting-Cards-BIG.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			'session':CheckUserSession(request),
			'checksession':1
			})
	return render(request,'allproducts.html',dic)
def proceedfororder(request):
	lt=[]
	try:
		pid=request.GET.get('cid')
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
				'checksession':1}
		obj=ProductDesignData.objects.filter(Product_ID=pid)
		for x in obj:
			d={'did':x.Design_ID,
				'image':x.Design_Image.url}
			lt.append(d)
		dic.update({'designs':lt})
		obj=ProductData.objects.filter(Product_ID=pid)
		for i in obj:
			dic.update({
			'Product_ID':i.Product_ID,
			'Product_Name':i.Product_Name,
			'Product_Paper_Type':i.Product_Paper_Type,
			'Product_Category':i.Product_Category,
			'Product_Thickness':i.Product_Thickness,
			'Product_Lamination':i.Product_Lamination,
			'Product_Quantity':i.Product_Quantity,
			'Product_Print_Sides':i.Product_Print_Sides,
			'Product_Color':i.Product_Color,
			'Product_Size':i.Product_Size,
			'Product_Price':i.Product_Price})
		return render(request,'orderdetails.html', dic)	
	except:
		return redirect('/userlogin/')