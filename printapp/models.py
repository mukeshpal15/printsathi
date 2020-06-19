from django.db import models
from datetime import date
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'

class PaperTypeData(models.Model):
	Paper_ID=models.CharField(max_length=100)
	Paper_Name=models.CharField(max_length=50)
	class Meta:
		db_table="PaperTypeData"

class ProductData(models.Model):
	Product_ID=models.CharField(max_length=100)
	Product_Name=models.CharField(max_length=100)
	Product_Paper_Type=models.CharField(max_length=100)
	Product_Category=models.CharField(max_length=100)
	Product_Thickness=models.CharField(max_length=100)
	Product_Lamination=models.CharField(max_length=100)
	Product_Quantity=models.CharField(max_length=100)
	Product_Print_Sides=models.CharField(max_length=100)
	Product_Color=models.CharField(max_length=100)
	Product_Size=models.CharField(max_length=100)
	Product_Price=models.CharField(max_length=100)
	Product_Status=models.CharField(max_length=100)
	class Meta:
		db_table="ProductData"

class ProductDesignData(models.Model):
	Design_ID=models.CharField(max_length=100)
	Product_ID=models.CharField(max_length=100)
	Design_Image=models.ImageField(upload_to="productdesignes/")
	class Meta:
		db_table="PropertyDesignData"

class OrderData(models.Model):
	Order_ID=models.CharField(max_length=100)
	Order_Date=models.DateField(auto_now=True)
	Product_ID=models.CharField(max_length=100)
	User_ID=models.CharField(max_length=100)
	Design_ID=models.CharField(max_length=100)
	Payment_ID=models.CharField(max_length=100)
	multiply_by_quantity=models.CharField(max_length=100)
	Detail_File=models.FileField(upload_to="orderdetailfile/", default='')
	Name=models.CharField(max_length=100, default='')
	companyname=models.CharField(max_length=100, default='')
	companygmail=models.CharField(max_length=100, default='')
	GSTN=models.CharField(max_length=100, default='')
	ph1=models.CharField(max_length=100, default='')
	ph2=models.CharField(max_length=100, default='')
	address=models.CharField(max_length=1000, default='')
	otherdetails=models.CharField(max_length=1000, default='')
	Order_Status=models.CharField(max_length=100)
	Total_Amount=models.CharField(max_length=100)
	Amount_to_Pay=models.CharField(max_length=100)
	Rest_Amount=models.CharField(max_length=100)
	class Meta:
		db_table="OrderData"

class CartData(models.Model):
	Cart_ID=models.CharField(max_length=100)
	Order_ID=models.CharField(max_length=50)
	User_Email=models.CharField(max_length=100)
	class Meta:
		db_table="CartData"

class UserData(models.Model):
	User_ID=models.CharField(max_length=100)
	User_First_Name=models.CharField(max_length=100)
	User_Last_Name=models.CharField(max_length=100)
	User_Gender=models.CharField(max_length=100)
	User_Email=models.CharField(max_length=100)
	User_Phone=models.CharField(max_length=100)
	User_Address=models.CharField(max_length=1000)
	User_City=models.CharField(max_length=100)
	User_State=models.CharField(max_length=100)
	User_Password=models.CharField(max_length=100)
	conditions=models.CharField(max_length=100)
	class Meta:
		db_table="UserData"

class ResellerData(models.Model):
	Reseller_ID=models.CharField(max_length=100)
	Reseller_First_Name=models.CharField(max_length=100)
	Reseller_Last_Name=models.CharField(max_length=100)
	Reseller_Gender=models.CharField(max_length=100)
	Reseller_Email=models.CharField(max_length=100)
	Reseller_Phone=models.CharField(max_length=100)
	Reseller_Address=models.CharField(max_length=1000)
	Reseller_City=models.CharField(max_length=100)
	Reseller_State=models.CharField(max_length=100)
	Reseller_GSTIN=models.CharField(max_length=100)
	Reseller_PAN=models.CharField(max_length=100)
	Reseller_Password=models.CharField(max_length=100)
	Reseller_Status=models.CharField(max_length=100)
	Adhaar=models.ImageField(upload_to="reselleradhaar/")
	Profile=models.ImageField(upload_to="resellerprofile/")
	conditions=models.CharField(max_length=100)
	class Meta:
		db_table="ResellerData"



class gallery(models.Model):
	Design_ID=models.CharField(max_length=100)
	galleryimage=models.ImageField(upload_to="gallerypics/")
	class Meta:
		db_table="gallery"
