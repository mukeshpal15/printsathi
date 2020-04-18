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
	Product_Status=models.CharField(max_length=100)
	class Meta:
		db_table="ProductData"

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
	class Meta:
		db_table="UserData"