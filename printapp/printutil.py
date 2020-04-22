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
		}
		sub=ProductDesignData.objects.filter(Product_ID=i.Product_ID)
		for j in sub:
			b=j.Design_Image.url
			break
		dic.update({'image':b})
		lt1.append(dic)	
	return lt1