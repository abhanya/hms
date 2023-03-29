from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('pathom',views.pat_home,name="phome"),
    path('pbookhis',views.pat_bookinghistory,name="history"),
    path('pending',views.pat_pendings,name="pending"),
    path('booking',views.pat_booking,name="booking"),
    path('pprofile',views.pat_profile,name="profile"),
    path('getdoc',views.get_doctor,name="getdoctor"),
    path('changepassword',views.password,name="password"),
    path('plogout', views.pat_logout, name='plogout'),
    path('viewpresc/<int:bid>',views.pat_viewpres,name="viewprescription"),    
]