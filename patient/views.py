from django.shortcuts import render,redirect
from common. models import Patient,Doctor
from doctor. models import Description
from projectadmin. models import Department
from . models import Booking
from django.http import JsonResponse
from .auth_gaurd import auth_patient

# Create your views here.
@auth_patient
def pat_home(request):
    patientdata = Patient.objects.get(id = request.session['patient'])
    return render(request,'pages/patienthome.html',{'pdata':patientdata})

@auth_patient
def pat_booking(request):
    msg=""
    patient_info = Patient.objects.get(id=request.session['patient'])
    doctors = Doctor.objects.values('id','doc_name')
    Booking_info = Department.objects.values('id','departments')

    print(doctors)
    if request.method == 'POST':
        
        sym = request.POST['symptoms']
        cuns = request.POST['consultion']
        doc = request.POST['doct']
        date = request.POST['date']

        doctor_obj = Doctor.objects.get(id=doc)
        dep_obj = Department.objects.get(id=cuns)
        if not Booking.objects.filter(patient= patient_info,symptoms = sym).exists():
        
            booking = Booking(patient=patient_info,doctor=doctor_obj,cunsultion_type=dep_obj,symptoms = sym,booking_date = date)
            
            booking.save()

            request.session['booking'] = booking.id

            msg="successfully Booked "
        else:
            msg ="already booked"
    context = {
            'patinfo':patient_info,
            'bookinfo':Booking_info,
            'doctors':doctors,
            'msg':msg,
        }
    
    return render(request,'pages/booking.html',context)

def pat_profile(request):
    msg = ''
    patientdata = Patient.objects.get(id = request.session['patient'])

    if request.method=='POST':
        patient = Patient.objects.get(id = request.session['patient'])

        pname = request.POST['p_name']
        pemail = request.POST['p_email']
        paddress = request.POST['p_address']
        phone_number = request.POST['p_number']
        pgender = request.POST['p_gender']
        page = request.POST['page']

        patient.pat_name = pname
        patient.pat_email = pemail
        patient.pat_address = paddress
        patient.pat_phone = phone_number
        patient.pat_gender = pgender
        patient.age = page
        
        patient.save()
        msg = 'Profile updated successfully'
        return redirect("patient:phome")
    return render(request,'pages/patprofile.html',{'pdata':patientdata,'msg':msg})

def pat_bookinghistory(request):
    booking_info = Booking.objects.filter(status ="t",patient_id=request.session['patient'])
    return render(request,'pages/booking_history.html',{'binfo':booking_info})

def pat_pendings(request):
    booking_info = Booking.objects.filter(status ="f",patient_id=request.session['patient'])
    return render(request,'pages/pendings.html',{'binfo':booking_info})

def pat_viewpres(request,bid):
    prescriptions = Description.objects.get(Booking_id=bid)
    print(prescriptions)
    return render(request,'pages/view_prescribtion.html',{ 'pres':prescriptions})

def get_doctor(request):
    depid = request.POST['keydep']
    doctors = Doctor.objects.filter(department_id = depid)
    doclist=[{'id':doctor.id,'name':doctor.doc_name} for doctor in doctors]
    return JsonResponse({'data':doclist})

def password(request):
    msg=""
    pat_data = Patient.objects.get(id=request.session['patient'])
    if request.method == 'POST':
        patient = Patient.objects.get(id = request.session['patient'])

        current_pass = request.POST['current_pass'] 
        new_pass = request.POST['new_pass'] 
        confirm_pass = request.POST['confirm_pass']

        if patient.pat_pass == current_pass:

            if new_pass == confirm_pass:
                 patient.pat_pass = new_pass
                 patient.save()
                 msg = 'Password changed succesfully'

            else:
                msg = 'Password does not match'

        else:
            msg = 'Incorrect Password'
    context =  {'msg':msg,
                'data': pat_data,
                }
    return render(request,'pages/password.html',context)

def pat_logout(request):
    del request.session['patient']
    request.session.flush() 
    return redirect('common:home')

# def pat_logout(request):
#     patient_id = request.session['patient']
#     if 'patient' in request.session:
#         del request.session['patient']
#     print(patient_id)
#     return redirect('common:home')

