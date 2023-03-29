from django.urls import path
from . import views

app_name = 'projectadmin'

urlpatterns = [
    path('docreg',views.hos_docregistration,name="docregistration"),   
    path('adminhome',views.hos_adminhom,name="adhome"),   
    path('doclist',views.hos_doctorlist,name="dlist"),   
    path('patlist',views.hos_patientlist,name="plist"),   
    path('department',views.hos_adddeprt,name="department"),
    path('approvdoc/<int:did>',views.docappr,name="approvdoc"),
    path('apprpage',views.approvepage,name="approvpage"),
    path('disapprove/<int:did>',views.docdisappr,name="dispprove"),
    path('remove/<int:did>',views.docremove,name="removedoctor"),
    path('removepatient/<int:pid>',views.patremove,name="removepatient"),
    path('adminlogin',views.admin_login,name="loginpage"),   
    path('logout',views.admin_logout,name="logout"),   

]