from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin



@admin.register(UserData)
class UserData(ImportExportModelAdmin):
	pass
@admin.register(ResellerData)
class ResellerData(ImportExportModelAdmin):
	pass

@admin.register(ProductData)
class ProductData(ImportExportModelAdmin):
	pass

@admin.register(ProductDesignData)
class ProductDesignData(ImportExportModelAdmin):
	pass

@admin.register(OrderData)
class OrderData(ImportExportModelAdmin):
	pass

@admin.register(gallery)
class gallery(ImportExportModelAdmin):
	pass

@admin.register(Testimonial)
class Testimonial(ImportExportModelAdmin):
	pass
@admin.register(Productdesign)
class Productdesign(ImportExportModelAdmin):
	pass
@admin.register(Rating)
class Rating(ImportExportModelAdmin):
	pass
