from django.core.paginator import *
from django.shortcuts import render, redirect
from django.conf import  settings
from django.urls import path
from printapp.models import *
from django.conf import  settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import *
import uuid
from django.contrib.auth import logout
from django.core.mail import EmailMessage
from printapp.printutil import *
from printapp.form import *
from wsgiref.util import FileWrapper
import mimetypes
import os

def index(request):
	dic={'session':CheckUserSession(request),
			'checksession':1,
			'sessionre':CheckResellerSession(request),
			'checksessionre':2,'detail':GetProductDetail(),
			'cartcount':GetCartCount(request)}
	return render(request, 'index.html', dic)		
def aboutus(request):
	dic={'session':CheckUserSession(request),
			'checksession':1,
			'checksessionre':2,
			'cartcount':GetCartCount(request)}
	return render(request, 'about-us.html',dic)
def allproducts(request):
	dic={'session':CheckUserSession(request),
			'checksession':1,
			'checksessionre':2,
			'cartcount':GetCartCount(request)}
	return render(request, 'allproducts.html',dic)
def category(request):
	dic={'session':CheckUserSession(request),
			'checksession':1,
			'checksessionre':2,
			'cartcount':GetCartCount(request)}
	return render(request, 'category.html',dic)
def cms(request):
	dic={'session':CheckUserSession(request),
			'checksession':1,
			'checksessionre':2,
			'cartcount':GetCartCount(request)}
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
				'checksession':1,
				'checksessionre':2,
				'cartcount':GetCartCount(request)})
	return render(request, 'productdetails.html',dic1)
def adminlogin(request):
	return render(request,'adminlogin.html',{})
def addproducts(request):
	return render(request, 'addproducts.html',{})
def userlogin(request):
	dic={'session':CheckUserSession(request),
		'checksession':1,
		'cartcount':GetCartCount(request)}
	return render(request, 'userlogin.html',dic)
def userregistration(request):
	dic={'session':CheckUserSession(request),
		'checksession':1,
		'cartcount':GetCartCount(request)}
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
		pp='+91'+request.POST.get('Phone Number')
		if UserData.objects.filter(User_Email=request.POST.get('Email'),User_Phone=pp).exists():
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
				User_Phone=pp,
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
			#snp=send_sms(pp,msg)
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
					'checksession':1,
					'cartcount':GetCartCount(request)}
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
			for i in obj:
				pp=i.User_Phone
				break
			for x in obj:
				dic={'fname': x.User_First_Name,
				'lname': x.User_Last_Name,
				'email': x.User_Email,
				'phone': x.User_Phone,
				'address': x.User_Address,
				'city': x.User_City,
				'state': x.User_State,
				'session':CheckUserSession(request),
				'checksession':1,
				'cartcount':GetCartCount(request)
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
			#snp=send_sms(pp,msg)
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
				'checksession':1,
				'cartcount':GetCartCount(request)
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
				'checksession':1,
				'cartcount':GetCartCount(request)
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
						'checksession':1,
						'cartcount':GetCartCount(request),
						'odata':GetOrderDetails(x.User_ID)
					}
				return render(request,'profile.html',dic)
			else:
				return HttpResponse('<h1>Error 404 NOT FOUND</h1>')	
		except:
			if ResellerData.objects.filter(Reseller_Email=request.session['re_email']).exists():
				dic={}
				obj=ResellerData.objects.filter(Reseller_Email=request.session['re_email'])
				for x in obj:
					dic={'fname': x.Reseller_First_Name,
						'lname': x.Reseller_Last_Name,
						'email': x.Reseller_Email,
						'phone': x.Reseller_Phone,
						'address': x.Reseller_Address,
						'city': x.Reseller_City,
						'state': x.Reseller_State,
						'sessionre':CheckResellerSession(request),
						'checksessionre':2,
						'cartcount':GetCartCount(request)
					}
				return render(request,'resellerprofile.html',dic)
			else:
				return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
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
def adminorderdetails(request):
	if request.method=="POST":
		dic={'data':GetOrderDetailsAdmin(),
			'data2':GetOrderDetailsAdmin2()}
		return render(request, 'adminorderdetail.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def downloadfile(request):
	if request.method=="POST":
		obj=OrderData.objects.filter(Order_ID=request.POST.get('oid'))
		file_path=''
		for x in obj:
			file_name = x.Detail_File.name
		file_path = settings.MEDIA_ROOT +'/'+ file_name
		file_wrapper = FileWrapper(open(file_path,'rb'))
		file_mimetype = mimetypes.guess_type(file_path)
		response = HttpResponse(file_wrapper, content_type=file_mimetype )
		response['X-Sendfile'] = file_path
		response['Content-Length'] = os.stat(file_path).st_size
		response['Content-Disposition'] = 'attachment; filename=%s' % file_name 
		return response
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

@csrf_exempt
def removeorder(request):
	if request.method=="POST":
		obj=OrderData.objects.filter(Order_ID=request.POST.get('oid'))
		obj.update(Order_Status="Completed")
		dic={'data':GetOrderDetailsAdmin(),
			'data2':GetOrderDetailsAdmin2()}
		return render(request, 'adminorderdetail.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')


@csrf_exempt
def logout(request):
	
	try:	
		
		del request.session['user_email']
		request.session.flush()
		return redirect('/index/')
	except:
		del request.session['re_email']
		request.session.flush()
			
		return redirect('/index/')
	
def resellerregistration(request):
	dic={'sessionre':CheckUserSession(request),
		'checksession':1,
		'cartcount':GetCartCount(request)}
	return render(request,'resellerregistration.html',dic)
@csrf_exempt
def savereseller(request):
	if request.method=="POST":
		u="R00"
		D='Deactive'
		x=1
		uid=u+str(x)
		while ResellerData.objects.filter(Reseller_ID=uid).exists():
			x=x+1
			uid=u+str(x)
		x=int(x)
		pp='+91'+request.POST.get('Phone Number')
		if ResellerData.objects.filter(Reseller_Email=request.POST.get('Email'), Reseller_Phone=pp).exists():
			dic={'msg':"Reseller Already Registered"}
			return render(request, 'resellerregistration.html',dic)
		elif ResellerData.objects.filter(Reseller_Phone=pp).exists():
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
							Reseller_Phone=pp,
							Reseller_Address=request.POST.get('Address'),
							Reseller_City=request.POST.get('City'),
							Reseller_State=request.POST.get('State'),
							Reseller_GSTIN=request.POST.get('GSTIN'),
							Reseller_PAN=request.POST.get('PAN'),
							Reseller_Password=password,
							Reseller_Status=D,
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
			#snp=send_sms(pp,msg)
			dic={'msg':"Reseller Registered Successfully",
				'msg1':"Your password has been sent to your email."}
			return render(request, 'resellerregistration.html',dic)
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
def resellerlogin(request):
	dic={'sessionre':CheckResellerSession(request),
		'checksessionre':2}
	return render(request, 'resellerlogin.html',dic)

@csrf_exempt
def resellerlog(request):
	if request.method=='POST':
		d='Active'
		check=1
		dic={}
		e=request.POST.get('email')
		p=request.POST.get('pass')
		if ResellerData.objects.filter(Reseller_Email=e,Reseller_Password=p):
			request.session['re_email'] = request.POST.get('email')
			obj=ResellerData.objects.filter(Reseller_Email=e)
			for i in obj:
				a=i.Reseller_Status
				break
			if a==d:
				for x in ResellerData.objects.filter(Reseller_Email=request.session['re_email']):
					dic={'fname': x.Reseller_First_Name,
						'lname': x.Reseller_Last_Name,
						'email': x.Reseller_Email,
						'phone': x.Reseller_Phone,
						'address': x.Reseller_Address,
						'city': x.Reseller_City,
						'state': x.Reseller_State,
						'sessionre':CheckResellerSession(request),
						'checksessionre':2,
						'cartcount':GetCartCount(request)}
					return render(request,'resellerprofile.html',dic)
				
			else:
				dic={'msg':'Your account is deactivated. Please wait admin response',}
				return render(request,'resellerlogin.html',dic)
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
				'sessionre':CheckResellerSession(request),
				'checksessionre':2,
				'cartcount':GetCartCount(request)
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
			for i in obj:
				pp=i.Reseller_Phone
				break
			for x in obj:
				dic={'fname': x.Reseller_First_Name,
				'lname': x.Reseller_Last_Name,
				'email': x.Reseller_Email,
				'phone': x.Reseller_Phone,
				'address': x.Reseller_Address,
				'city': x.Reseller_City,
				'state': x.Reseller_State,
				'sessionre':CheckResellerSession(request),
				'checksessionre':2,
				'cartcount':GetCartCount(request)
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
			#snp=send_sms(pp,msg)
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
				'sessionre':CheckResellerSession(request),
				'checksessionre':2,
				'cartcount':GetCartCount(request)
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
			pp=x.Reseller_Phone
			break
		msg = '''Hi there!
Your Reseller Account has been activated successfully,

Password : '''+p+'''

Thanks & Regards,
Printsathi'''
		sub='Congratulations! Reseller Account Activated Successfully'
		email = EmailMessage(sub, msg, to=[e])
		email.send()
		#snp=send_sms(pp,msg)
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
	try:
		try:
			n=request.session['user_email']
			if UserData.objects.filter(User_Email=n).exists():
				dic=getdatacatagary(cname)
				dic.update({'session':CheckUserSession(request),
							'checksession':1,
							'cartcount':GetCartCount(request),
							'sessionre':CheckResellerSession(n),
							'checksessionre':2,})
				return render(request,'allproducts.html',dic)
		except:
			n=request.session['re_email']
			if ResellerData.objects.filter(Reseller_Email=n).exists():
				dic=getdatacatagary(cname)
				dic.update({'session':CheckUserSession(request),
							'checksession':1,
							'cartcount':GetCartCount(request),
							'sessionre':CheckResellerSession(n),
							'checksessionre':2,})
				return render(request,'allproducts.html',dic)
	except:
		dic=getdatacatagary(cname)
		dic.update({'session':CheckUserSession(request),
					'checksession':1,
					'cartcount':GetCartCount(request),
					'sessionre':1,
					'checksessionre':2,})
		return render(request,'allproducts.html',dic)
	
def userforgotpass(request):
	return render(request, 'userforgotpass.html',{})

def user_send_pass(request):
	if request.method=="POST":
		n=request.POST.get('email')
		if UserData.objects.filter(User_Email=n).exists():
			obj=UserData.objects.filter(User_Email=n)
			for i in obj:
				p=i.User_Password
				pp=i.User_Phone
				break
			msg = '''hello sir,


Your Password is : '''+p+'''


Thanks & Regards,
Printsathi'''
			sub='Your Account Password'
			email = EmailMessage(sub, msg, to=[n])
			email.send()
			#print(pp)
			#snp=send_sms(pp,msg)
			return HttpResponse("<script> alert('Your Password has been sent to your mail Id and Phone'); window.location.replace('/userlogin/') </script>")
		else:
			msg='Please enter the valid mail Id'
			
			return render(request,'userforgotpass.html',{'msg':msg})
def resellerforgotpass(request):
	return render(request, 'resellerforgotpass.html',{})

def reseller_send_pass(request):
	if request.method=="POST":
		n=request.POST.get('email')
		if ResellerData.objects.filter(Reseller_Email=n).exists():
			obj=ResellerData.objects.filter(Reseller_Email=n)
			for i in obj:
				p=i.Reseller_Password
				pp=i.Reseller_Phone
				break
			msg = '''hello sir,


Your Password is : '''+p+'''


Thanks & Regards,
Printsathi'''
			sub='Your Account Password'
			email = EmailMessage(sub, msg, to=[n])
			email.send()
			#snp=send_sms(pp,msg)
			return HttpResponse("<script> alert('Your Password has been sent to your mail Id and Phone'); window.location.replace('/resellerlogin/') </script>")
		else:
			msg='Please enter the valid mail Id'
			
			return render(request,'resellerforgotpass.html',{'msg':msg})





#Payment Gateway Functions
import razorpay
#Working on Test Keys
razorpay_client = razorpay.Client(auth=("rzp_test_30ncLAFfGjrh3N", "l6tOEr4l26jJqhTHwXhny0eX"))
razorpay_client.set_app_details({"title" : "Printsathi", "version" : "1.0"})

#Step 1
def proceedfororder(request):
	lt=[]
	try:
		pid=request.GET.get('cid')
		obj=UserData.objects.filter(User_Email=request.session['user_email'])
		for x in obj:
			dic={'uid': x.User_ID,
				'session':CheckUserSession(request),
				'checksession':1,
				'sessionre':CheckResellerSession(request),
				'checksessionre':2}
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
			'Product_Price':i.Product_Price,
			'cartcount':GetCartCount(request)})
		return render(request,'orderdetails.html', dic)	
	except:
		return redirect('/userlogin/')

#Step 2






@csrf_exempt
def orderdatasave(request):
	if request.method=="POST":
		did=request.POST.get('design')
		uid=request.POST.get('uid')
		pid=request.POST.get('pid')
		dfile=request.FILES['detailfile']
		o='OR00'
		x=1
		oid=o+str(x)
		while OrderData.objects.filter(Order_ID=oid).exists():
			x=x+1
			oid=o+str(x)
		x=int(x)
		obj=OrderData(
			Order_ID=oid,
			Product_ID=pid,
			User_ID=uid,
			Design_ID=did,
			Order_Status='Unpaid',
			Detail_File=dfile,
			Total_Amount='0',
			Amount_to_Pay='0',
			Rest_Amount='0'
			)
		obj.save()
		lt=[]
		dic={}
		userid=''
		tm=0
		obj1=UserData.objects.filter(User_Email=request.session['user_email'])
		for x in obj1:
			userid=x.User_ID
			break
		obj1=OrderData.objects.filter(User_ID=userid,Order_Status='Unpaid')
		for z in obj1:
			obj=ProductData.objects.filter(Product_ID=z.Product_ID)
			for x in obj:
				dic={
					'orderid':z.Order_ID,
					'name':x.Product_Name,
					'category':x.Product_Category,
					'price':x.Product_Price,
					'quantity':x.Product_Quantity,
				}
				tm=tm+int(x.Product_Price)
				obj2=ProductDesignData.objects.filter(Design_ID=did)
				for y in obj2:
					dic.update({
						'image':y.Design_Image.url,
						})
				lt.append(dic)
		obj1=OrderData.objects.filter(User_ID=userid,Order_Status='Unpaid')
		obj1.update(Total_Amount=str(tm),
			Amount_to_Pay=str((tm/100)*25),
			Rest_Amount=str(tm-((tm/100)*25)))
		return render(request,'cart.html',{'cartcount':GetCartCount(request),'cartdata':lt,'totalamount':tm,'count':len(lt)})
	else:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')

def opencart(request):
	lt=[]
	dic={}
	userid=''
	tm=0
	useremail=request.session['user_email']
	obj=UserData.objects.filter(User_Email=useremail)
	for x in obj:
		userid=x.User_ID
	obj1=OrderData.objects.filter(User_ID=userid,Order_Status='Unpaid')
	for z in obj1:
		obj=ProductData.objects.filter(Product_ID=z.Product_ID)
		for x in obj:
			dic={
				'orderid':z.Order_ID,
				'name':x.Product_Name,
				'category':x.Product_Category,
				'price':x.Product_Price,
				'quantity':x.Product_Quantity,
			}
			tm=tm+int(x.Product_Price)
			obj2=ProductDesignData.objects.filter(Design_ID=z.Design_ID)
			for y in obj2:
				dic.update({
					'image':y.Design_Image.url,
					})
			lt.append(dic)
	return render(request,'cart.html',{'cartdata':lt,'totalamount':tm,'count':len(lt)})





def proceedtopay(request):
	try:
		if UserData.objects.filter(User_Email=request.session['user_email']).exists():
			userid=''
			dic={}
			obj1=UserData.objects.filter(User_Email=request.session['user_email'])
			for x in obj1:
				userid=x.User_ID
				break
			o='CRT00'
			x=1
			oid=o+str(x)
			while CartData.objects.filter(Cart_ID=oid).exists():
				x=x+1
				oid=o+str(x)
			x=int(x)
			obj1=OrderData.objects.filter(User_ID=userid,Order_Status='Unpaid')
			for z in obj1:
				obj=CartData(Cart_ID=oid,Order_ID=z.Order_ID,User_Email=request.session['user_email'])
				obj.save()
				dic={'cid':oid,
					'tamount':z.Total_Amount,
					'pamount':z.Amount_to_Pay,
					'amounttopay':float(z.Amount_to_Pay)*100,
					'session':CheckUserSession(request),
					'checksession':1}
				request.session['cartid'] = oid
				obj=UserData.objects.filter(User_Email=request.session['user_email'])
				for x in obj:
					dic.update({
						'uname':x.User_First_Name+' '+x.User_Last_Name,
						'uemail':x.User_Email,
						'uphone':x.User_Phone
						})
				order_amount = int(dic['amounttopay'])
				order_currency = 'INR'
				order_receipt = dic['cid'] 
				options={
					'amount':order_amount,
					'currency':order_currency,
					'receipt':order_receipt,
					'payment_capture':'0'
				}
				dic.update(razorpay_client.order.create(options))
			return render(request,'proceedtopay.html',dic)
	except:
		return HttpResponse('<h1>Error 404 NOT FOUND</h1>')
#Step 4
@csrf_protect
@csrf_exempt
def app_charge(request):
	dic={}
	razorpay_order_id = request.POST.get('razorpay_order_id')
	razorpay_payment_id = request.POST.get('razorpay_payment_id')
	razorpay_signature = request.POST.get('razorpay_signature')
	params_dict = {
    'razorpay_order_id': razorpay_order_id,
    'razorpay_payment_id': razorpay_payment_id,
    'razorpay_signature': razorpay_signature}
	if razorpay_client.utility.verify_payment_signature(params_dict):
		obj=CartData.objects.filter(Cart_ID=request.session['cartid'])
		for x in obj:
			obj1=OrderData.objects.filter(Order_ID=x.Order_ID)
			obj1.update(Payment_ID=razorpay_payment_id,Order_Status='Paid')
			dic={'cid':x.Cart_ID,'pid':razorpay_payment_id}
		obj.delete()
		msg = '''Hi there!,
Your payment for Cart ID '''+request.session['cartid']+'''is successful!
Your Payment ID is '''+razorpay_payment_id+'''

Thanks & Regards,
Printsathi'''
		sub='Printsathi - Payment Successful'
		email = EmailMessage(sub, msg, to=[request.session['user_email']])
		email.send()
		return render(request,'paymentsuccess.html',dic)
	else:
		obj=CartData.objects.filter(Cart_ID=request.session['cartid'])
		for x in obj:
			print(x.Order_ID)
			obj1=OrderData.objects.filter(Order_ID=x.Order_ID)
			obj1.update(Payment_ID=razorpay_payment_id,Order_Status='Payment Failed')
			dic={'cid':x.Cart_ID,'pid':razorpay_payment_id}
		msg = '''Hi there!,
Your payment for Order ID '''+request.session['order_id']+'''is failed!
Your Payment ID is '''+razorpay_payment_id+'''
we apologize for this. Kindly send a mail to us regarding this problem.

Thanks & Regards,
Printsathi'''
		sub='Printsathi - Payment Failed'
		email = EmailMessage(sub, msg, to=[request.session['user_email']])
		email.send()
		return render(request,'paymentfailure.html',dic)

def cart(request):
	return render(request,'cart.html',{})
def deliveryboylogin(request):
	return render(request,'deliveryboylogin.html',{})
def deliveryboypannel(request):
	return render(request,'deliveryboypannel.html',{})
def adminorderdetail(request):
	return render(request,'adminorderdetail.html',{})