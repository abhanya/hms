from django.shortcuts import render,redirect
from common. models import Doctor,Patient
from . models import Department,HospitalAdmin
from patient. models import Booking
from django.http import JsonResponse

# Create your views here.

def hos_docregistration(request):
    msg=""
    depart = Department.objects.values('id','departments')
    if request.method == 'POST':
        dname = request.POST['d_name']
        daddr = request.POST['d_add']
        dgend = request.POST['d_gender']
        dphn = request.POST['dphon']
        dmail = request.POST['demail']
        ddob = request.POST['ddob']
        dcstate = request.POST['dstate']
        dspecial = request.POST['dspecial']
        dcuser = request.POST['duser']
        dcpass = request.POST['dpass']

        if not Doctor.objects.filter(doc_email= dmail).exists():

            new_doctor = Doctor(doc_name = dname, doc_address = daddr, doc_gender = dgend,doc_username = dcuser,
                                doc_phone = dphn, doc_email = dmail, doc_dob = ddob,
                                doc_state = dcstate, department_id = int(dspecial),doc_pass=dcpass,approve=True)

            new_doctor.save()
            return redirect('projectadmin:dlist')
        else:
            msg="email already exist !"

    return render(request,'pages/doctorregistration.html',{'bookinfo':depart,'msg':msg})

def hos_adddeprt(request):
    if request.method == 'POST':
        dep = request.POST['department']
        des = request.POST['description']

        department = Department(departments = dep, description = des)

        department.save()
    return render(request,'pages/add_department.html')

def hos_doctorlist(request):
    doctors = Doctor.objects.filter(approve = True)  
    return render(request,'pages/doctorlist.html',{'doclist':doctors})

def hos_patientlist(request):
    pats =  Patient.objects.all()
    bookingdet = Booking.objects.filter()
    return render(request,'pages/patientlist.html',{'patlist':pats,'book':bookingdet})
def patremove(request,pid):
    patlist = Patient.objects.get(id = pid)
    patlist.delete()
    return redirect('projectadmin:plist')

def hos_adminhom(request):
    return render(request,'pages/adminhome.html')


def approvepage(request):
    docs = Doctor.objects.filter(approve = False)
    return render(request,'pages/approvedoctor.html',{'doclist':docs})

def docappr(request,did):
    doctor = Doctor.objects.get(id=did)   
    doctor.approve = True
    doctor.save()
    return redirect('projectadmin:approvpage')

def docdisappr(request,did):
    doctorlist = Doctor.objects.get(id = did)
    doctorlist.delete()
    return redirect('projectadmin:approvpage')

def docremove(request,did):
    doctorlist = Doctor.objects.get(id = did)
    doctorlist.delete()
    return redirect('projectadmin:dlist')

def patemail_exist(request):
    email = request.POST['email']   
    status = Patient.objects.filter(pat_email = email).exists()
    return JsonResponse({'status':status})

def admin_login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            hospitaladmin = HospitalAdmin.objects.get(username = username, password = password)
            request.session['hospitaladmin'] = hospitaladmin.id
            return redirect('projectadmin:adhome')
        except:
            msg ='Incorrect Username or password !'
    return render(request,'pages/admin_login.html',{'msg':msg})


def admin_logout(request):
    del request.session['hospitaladmin']
    request.session.flush() 
    return redirect('projectadmin:loginpage')