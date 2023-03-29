from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('commonhome',views.hos_comm,name="home"),
    path('dlogin',views.hos_doclogin,name="doclog"),
    path('plogin',views.hos_patlogin,name="patlog"),
    path('reg',views.hos_registration,name="registration"),
    path('docreg',views.hos_docregistration,name="docregistration"),  
    path('emailexist',views.email_exist,name="emailexist"),
    path('patemailexist',views.patemail_exist,name="pemailexist"),
]