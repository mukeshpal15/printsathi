from django.db import models
from datetime import date
from django.conf import settings
TIME_FORMAT = '%d.%m.%Y'

class PaperTypeData(models.Model):
	Paper_ID=models.CharField(max_length=100)
	Paper_Name=models.CharField(max_length=50)
	class Meta:
		db_table="PaperTypeData"
