from django.shortcuts import render,redirect
from . models import Patient,Doctor
from projectadmin. models import Department
from django.http import JsonResponse


# Create your views here.

def hos_comm(request):
    return render(request,'pages/commonhome.html')

def hos_doclogin(request):
    msg = ''
    if request.method == 'POST':
        dcmail = request.POST['dmail']
        dcpas = request.POST['dpass']
        try:
            doctor = Doctor.objects.get(doc_email = dcmail, doc_pass = dcpas,approve = True)
            request.session['doctor'] = doctor.id
            return redirect('doctor:dhome')
        except:
            msg ='Incorrect Username or password !'
    return render(request,'pages/doctorlogin.html',{'msg':msg})

def hos_patlogin(request):
    msg = ''
    if request.method == 'POST':
        ptmail = request.POST['pmail']
        ptpas = request.POST['ppass']
        try:
            patient = Patient.objects.get(pat_email = ptmail, pat_pass = ptpas)
            request.session['patient'] = patient.id
            return redirect('patient:phome')
        except:
            msg ='Incorrect Username or password !'
    return render(request,'pages/patientlogin.html',{'msg':msg})

def hos_registration(request):
    msg=""
    if request.method == 'POST':
        pname = request.POST['p_name']
        paddr = request.POST['p_add']
        pgend = request.POST['p_gender']
        pphn = request.POST['pphon']
        pmail = request.POST['pemail']
        ppass = request.POST['p_pass']
        page = request.POST['page']

        if not Patient.objects.filter(pat_email= pmail).exists():
            new_patient = Patient(pat_name = pname, pat_address = paddr, pat_gender = pgend,
                               pat_phone = pphn,  pat_email= pmail, pat_pass = ppass, age = page)

            new_patient.save()
            return redirect('common:patlog')
        else:
            msg="email already exist !,please try using another email address"
    return render(request,'pages/registration.html')

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
        dspecial = request.POST['special']
        dcuser = request.POST['duser']
        dcpass = request.POST['dpass']

        if not Doctor.objects.filter(doc_email= dmail).exists():

            new_doctor = Doctor(doc_name = dname, doc_address = daddr, doc_gender = dgend,doc_username = dcuser,
                                doc_phone = dphn, doc_email = dmail, doc_dob = ddob,
                                doc_state = dcstate, department_id = int(dspecial),doc_pass = dcpass)

            new_doctor.save()
            return redirect('common:doclog')
        else:
            msg="email already exist !"

    return render(request,'pages/docreg.html',{'bookinfo':depart,'msg':msg})

def email_exist(request):
    email = request.POST['email']   
    status = Doctor.objects.filter(doc_email = email).exists()
    return JsonResponse({'status':status})

def patemail_exist(request):
    email = request.POST['email']   
    status = Patient.objects.filter(pat_email = email).exists()
    return JsonResponse({'status':status})



