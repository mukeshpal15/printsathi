from django.contrib import admin
from .models import *

admin.site.register(UserData)
admin.site.register(ResellerData) 
admin.site.register(ProductData) 
admin.site.register(ProductDesignData) 
admin.site.register(OrderData) 
# Register your models here.
admin.site.register(gallery)