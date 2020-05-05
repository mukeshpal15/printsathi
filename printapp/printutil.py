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
		if UserData.objects.filter(User_Email=request.session['user_email']).exists():
			return 1
		else:
			return 0
	except:
		return 0

def CheckResellerSession(n):
	try:
		if ResellerData.objects.filter(Reseller_Email=request.session['re_email']).exists():
			return 2
		else:
			return 0
	except:
		return 0
def delresellersession(request):
	if ResellerData.objects.filter(Reseller_Email=request.session['re_email']).exists():
		del request.session['re_email']
		request.session.flush()
		return 0
	else:
		request.session['re_email']=0
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
	for a in list(set(zip(pid))):
		for x in a:
			dic={'id':x,
				'count':GetCount(x),
				}
			lt.append(dic)
	return lt
def GetProductDetail():
	obj=ProductData.objects.filter(Product_Status='Active')
	lt1=[]
	b=''
	for i in obj:
		dic={'Product_ID':i.Product_ID,
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
		}
		sub=ProductDesignData.objects.filter(Product_ID=i.Product_ID)
		for j in sub:
			b=j.Design_Image.url
			break
		dic.update({'image':b})
		lt1.append(dic)	
	return lt1

def GetAgainProductDetail(pid):
	obj=ProductData.objects.filter(Product_ID=pid)
	dic={}
	lt=[]
	for i in obj:
		dic={'Product_ID':i.Product_ID,
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
			}
		sub=ProductDesignData.objects.filter(Product_ID=pid)
		i=0
		img={}
		for j in sub:
			img.update({'image':j.Design_Image.url,
						'imgid':str(i)})
			i=i+1
			lt.append(img)
		dic.update({'img':lt})
		for j in sub:
			dic.update({'coverimage':j.Design_Image.url,
						'coverid':'cover'})
			break
	return dic

def GetProductDetailByCategory(cname):
	obj=ProductData.objects.filter(Product_Status='Active',Product_Category=cname)
	lt1=[]
	b=''
	for i in obj:
		dic={'Product_ID':i.Product_ID,
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
			'Price':(int(i.Product_Price)*90)/100,
		}

		sub=ProductDesignData.objects.filter(Product_ID=i.Product_ID)
		for j in sub:
			b=j.Design_Image.url
			break
		dic.update({'image':b})
		lt1.append(dic)	
	return lt1
	
from twilio.rest import Client
def send_sms(p,m):
	account_sid = 'AC80c7b1700ce56e8c0a47a3c3195c35c7'
	auth_token = '32926aeabd1e311c1bc60d07c26b3697'
	client = Client(account_sid, auth_token)
	message = client.messages \
	    .create(
	         body=m,
	         messaging_service_sid='MGca893f5b3d0d38edf1ca1edd21b8c3a2',
		 	 from_='+15592380575',
	         to=p
	     )
	return (message.sid)



def getdatacatagary(cname):

	dic={'data':GetProductDetailByCategory(cname)}
	if cname=='Business Cards':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/Visiting-Cards-BIG.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic

	elif cname=='Office Stationary':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/40307043-back-to-school-blackboard-with-pencilbox-and-school-equipment-on-table.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			
			})
		return dic

	elif cname=='Marketing Tool':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/pexels-photo-313691-1024x768.jpeg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic

	elif cname=='Doctoor Tools':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/download.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic

	elif cname=='Invitation Cards':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic

	elif cname=='Apparels/Gifts':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	else:
		return 0
def GetOrderDetails(userid):
	obj=OrderData.objects.filter(User_ID=userid)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'orderid':x.Order_ID,
		'paymentid':x.Payment_ID,
		'status':x.Order_Status
		}
		obj1=ProductData.objects.filter(Product_ID=x.Product_ID)
		for y in obj1:
			dic.update({
				'pname':y.Product_Name,
				'pprice':y.Product_Price,
				'pcategory':y.Product_Category
				})
		obj2=ProductDesignData.objects.filter(Design_ID=x.Design_ID)
		for z in obj2:
			dic.update({
				'pimg':z.Design_Image.url
				})
		lt.append(dic)
	return lt

def GetCartCount(request):
	try:
		obj=UserData.objects.filter(User_Email=request.session['user_email'])
		userid=''
		for x in obj:
			userid=x.User_ID
		obj=OrderData.objects.filter(User_ID=userid,Order_Status='Unpaid')
		return len(obj)
	except:
		return 0