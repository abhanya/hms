from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
    path('dochom',views.doc_home,name="dhome"),
    path('addpres/<int:appointment_id>/<int:patient_id>',views.doc_addpresc,name="addpres"),
    path('appoinmnts',views.doc_appoinments,name="appoin"),
    path('dprofile',views.doc_profile,name="dprofile"),
    path('viewpat',views.doc_viewpat,name="viewpatients"),
    path('changepass',views.passwordchange,name="pass"),
    path('dlogout', views.doc_logout, name='dlogout'),
]