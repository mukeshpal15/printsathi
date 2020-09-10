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
from django.db.models import Q

def CheckUserSession(request):
	try:
		if UserData.objects.filter(User_Email=request.session['user_email']).exists():
			return 1
		else:
			return 0
	except:
		return 0

def CheckResellerSession(request):
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
			'Product_Type':i.Product_Type,
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
def Getsinglebusinesscrad():
	obj=ProductData.objects.filter(Product_Print_Sides='Single Sides', Product_Status='Active', Product_Category='Business Cards')
	
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

def Getbacktobackbusinesscrad():
	obj=ProductData.objects.filter(Product_Print_Sides='Both Sides', Product_Status='Active', Product_Category='Business Cards')
	
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

def Getsinglevisitingcrad():
	obj=ProductData.objects.filter(Product_Print_Sides='Single Sides', Product_Category='Visiting Cards')
	
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

def Getdoublevisitingcrad():
	obj=ProductData.objects.filter(Product_Print_Sides='Both Sides', Product_Category='Visiting Cards')
	
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

def spotlelinatedvisitingcrad():
	obj=ProductData.objects.filter(Product_Lamination='Gloss', Product_Category='Visiting Cards')
	
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
	obj=ProductData.objects.filter(Product_Status='Active',Product_Type=cname)
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

	elif cname=='Stationary':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/40307043-back-to-school-blackboard-with-pencilbox-and-school-equipment-on-table.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			
			})
		return dic

	elif cname=='Digital Marketing':
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

	elif cname=='Gift or Novelties':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Flex or Banner':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Promotional Tools':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='EnvelopesA4':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Envelopes10':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Letterpads':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Folders':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Files':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Stamps':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Notebooks':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Flyers':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Brochures':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Poster':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Banners':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Standers':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Tent Cards':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Vouchers':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Certificares':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Documents Pricing':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Stickers':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Product for Doctor':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Corporates Gifting':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Gift Bags':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Gift Boxes':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Calendars':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Diaries':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Coasters':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Mugs':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Engraved Pens':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Plastic Pens':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='BookPad':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Lanyards':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
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
	elif cname=='Canvas':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Banners':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Photo Frames':
		dic.update({
			'cname':cname,
			'cimage':'/static/images/cosmic-interactive-business-card.jpg',
			'cpic':'/static/images/47227_invitation-card-wedding-wallpapers-invitation-card-wedding_1600x1200_h.jpg',
			'clen':len(GetProductDetailByCategory(cname)),
			
			
			})
		return dic
	elif cname=='Polo T-shirt':
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
		obj2=Productdesign.objects.filter(Design_ID=x.Design_ID)
		for z in obj2:
			dic.update({
				'pimg':z.Design_Image.url
				})
		lt.append(dic)
	return lt

def GetCartCount(request):
	try:
		try:
			obj=UserData.objects.filter(User_Email=request.session['user_email'])
			userid=''
			for x in obj:
				userid=x.User_ID
			obj=OrderData.objects.filter(User_ID=userid,Order_Status='Unpaid')
			return len(obj)
		except:
			obj=ResellerData.objects.filter(Reseller_Email=request.session['re_email'])
			userid=''
			for x in obj:
				sellerid=x.Reseller_ID
			obj=OrderData.objects.filter(User_ID=sellerid,Order_Status='Unpaid')
			return len(obj)
	except:
		return 0

def GetOrderDetailsAdmin():
	dic={}
	lt=[]
	obj=OrderData.objects.filter(Order_Status='Paid')
	for x in obj:
		dic={
		'orderid':x.Order_ID,
		'orderdate':x.Order_Date,

		'payid':x.Payment_ID,
		'status':x.Order_Status,
		'totalamount':x.Total_Amount,
		'amounttopay':str((int(x.Total_Amount)/100)*25),
		'restamount':x.Rest_Amount
		}
		obj1=UserData.objects.filter(User_ID=x.User_ID)
		for y in obj1:
			dic.update({
				'cname':y.User_First_Name+' '+y.User_Last_Name,
				'cmail':y.User_Email,
				'cphone':y.User_Phone,
				'caddress':y.User_Address,
				'ccity':y.User_City,
				'cstate':y.User_State,
				})
		obj2=ProductData.objects.filter(Product_ID=x.Product_ID)
		for z in obj2:
			dic.update({
				'pname':z.Product_Name,
				'pcategory':z.Product_Type,
				})
		obj3=Productdesign.objects.filter(Design_ID=x.Design_ID)
		for w in obj3:
			dic.update({
				'design':w.Design_Image.url,
				})
		lt.append(dic)
		lt.reverse()
	return lt

def GetOrderDetailsAdmin2():
	dic={}
	lt=[]
	obj=OrderData.objects.filter(Order_Status='Completed')
	for x in obj:
		dic={
		'orderid':x.Order_ID,
		'orderdate':x.Order_Date,

		'payid':x.Payment_ID,
		'status':x.Order_Status,
		'totalamount':x.Total_Amount,
		'amounttopay':str((int(x.Total_Amount)/100)*25),
		'restamount':x.Rest_Amount
		}
		obj1=UserData.objects.filter(User_ID=x.User_ID)
		for y in obj1:
			dic.update({
				'cname':y.User_First_Name+' '+y.User_Last_Name,
				'cmail':y.User_Email,
				'cphone':y.User_Phone,
				'caddress':y.User_Address,
				'ccity':y.User_City,
				'cstate':y.User_State,
				})
		obj2=ProductData.objects.filter(Product_ID=x.Product_ID)
		for z in obj2:
			dic.update({
				'pname':z.Product_Name,
				'pcategory':z.Product_Category,
				})
		obj3=ProductDesignData.objects.filter(Design_ID=x.Design_ID)
		for w in obj3:
			dic.update({
				'design':w.Design_Image.url,
				})
		lt.append(dic)
		lt.reverse()
	return lt


def GetsingleOrderDetail(cname):
	dic={}
	lt=[]
	obj=OrderData.objects.filter(Order_ID=cname)
	for x in obj:
		obj5=ProductData.objects.filter(Product_ID=x.Product_ID)
		for y in obj5:
			if 'Business Cards' == y.Product_Type:
				qty=str(int(x.quantity)*int(x.multiply_by_quantity))
			else:
				qty=str(int(y.Product_Quantity)*int(x.multiply_by_quantity))
			break

		dic={
		'orderid':x.Order_ID,
		'orderdate':x.Order_Date,
		'name':x.Name,
		'company':x.companyname,
		'gmail':x.companygmail,
		'gstn':x.GSTN,
		'web':x.weblink,
		'ph1':x.ph1,
		'ph2':x.ph2,
		'address':x.address,
		'other':x.otherdetails,
		'paper':x.paper_weight,
		'Corner':x.Corner,
		'side':x.side,
		'quantity':qty,
		'lamination':x.lamination,
		'logo':x.logo.url,
		}
		try:
			dic.update({'file': x.Detail_File.url})
		except:
			dic.update({'file': 'media/Resellerpic/3.jpg'})

		obj1=UserData.objects.filter(User_ID=x.User_ID)
		for y in obj1:
			dic.update({
				'cname':y.User_First_Name+' '+y.User_Last_Name,
				'cmail':y.User_Email,
				'cphone':y.User_Phone,
				'caddress':y.User_Address,
				'ccity':y.User_City,
				'cstate':y.User_State,
				})
		obj2=ProductData.objects.filter(Product_ID=x.Product_ID)
		for z in obj2:
			dic.update({
				'pname':z.Product_Name,
				'pcategory':z.Product_Type,
				})
		obj3=Productdesign.objects.filter(Design_ID=x.Design_ID)
		for w in obj3:
			dic.update({
				'design':w.Design_Image.url,
				})
		lt.append(dic)
		
	return lt


def gettestidata():

	ob=Testimonial.objects.all()
	lt=[]
	dic={}
	for i in ob:
		dic={
			'Tid':i.testi_ID,
			'name':i.testiname,
			'pic':i.pic.url,
			'msg':i.msg
		}
		lt.append(dic)

	return lt

def banners():
	obj=Banner.objects.all()
	dic={}
	for i in obj:
		dic={
		'bnnr1':i.first.url,
		'bnnr2':i.second.url
		}
		break
	return dic

def feedbackrat():
	ob=UserData.objects.all()
	re=ResellerData.objects.all()
	lt=[]
	dic={}
	dic2={}
	for i in ob:
		if Rating.objects.filter(CustomerID=i.User_Email).exists():
			st=Rating.objects.filter(CustomerID=i.User_Email)
			for j in st:
				dic={
				'name':i.User_First_Name,
				'cmt':j.comment,
				'date':j.Date,
				'rat':int(j.star1)
				}
				lt.append(dic)

	for i in re:
		if Rating.objects.filter(CustomerID=i.Reseller_Email).exists():
			st=Rating.objects.filter(CustomerID=i.Reseller_Email)
			for j in st:
				dic={
				'name':i.Reseller_First_Name,
				'cmt':j.comment,
				'date':j.Date,
				'rat': int(j.star1)
				}
				lt.append(dic)
	print(lt)
	return lt

import math
def rating():
	st=Rating.objects.all()
	s=0
	t=0
	for i in st:
		s=s+1
		t=t+int(i.star1)
	f=math.floor(t/s)


	dic={'sum':s,
		'star':f}
	print(dic)
	return dic
