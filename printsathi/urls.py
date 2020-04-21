from django.contrib import admin
from django.urls import path
from printapp.views import *
from printapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    path('aboutus/',aboutus),
    path('allproducts/',allproducts),
    path('category/',category),
    path('cms/',cms),
    path('coomingsoon/',coomingsoon),
    path('howitworks/',howitworks),
    path('pricing/',pricing),
    path('productdetails/',productdetails),
    path('admindash/',admindash),
    path('adminlogin/',adminlogin),
    path('backtoadmindash/',backtoadmindash),
    path('addproducts/',addproducts),
    path('saveproducts/',saveproducts),
    path('deleteproducts/',deleteproducts),
    path('deactiveproducts/',deactiveproducts),
    path('addpapertype/',addpapertype),
    path('savepapertype/',savepapertype),
    path('deletepapertype/',DeletePaperType),
    path('userlogin/',userlogin),
    path('userregistration/',userregistration),
    path('saveuser/',saveuser),
    path('userlog/',userlog),
    path('changeuserpassword/',changeuserpassword),
    path('changeuserdetails/',changeuserdetails),
    path('myorders/',myorders),
    path('myordersdetails/',myordersdetails),
    path('myuseraccount/',myuseraccount),
    path('adddesigns/',adddesigns),
    path('savedesigns/',savedesigns),
    path('Resellerenter/',Resellerenter),
    path('resellerlogin/',resellerlogin),
    path('resellerlog/',resellerlog),
    path('changeresellerdetails/',changeresellerdetails),
    path('changeresellerpassword/',changeresellerpassword),
    path('logout/',logout),
    path('resellerregistration/',resellerregistration),
    path('savereseller/',savereseller),
    path('resellerdata/',resellerdata),
    path('reselleractive/',reselleractive),
    path('resellerdeactive/',resellerdeactive),
    path('opencategory/',opencategory),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
