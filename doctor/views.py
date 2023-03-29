from django.shortcuts import render,redirect
from patient. models import Booking
from doctor. models import Description
from common. models import Doctor,Patient



# Create your views here.

def doc_home(request):
    doctdata = Doctor.objects.get(id = request.session['doctor'])
    return render(request,'pages/doctorhome.html',{'doctdata':doctdata})
def doc_appoinments(request):
    appoinmnts = Booking.objects.filter(doctor = request.session['doctor'])
    return render(request,'pages/appoinments.html',{'appoinments':appoinmnts})    
   
def doc_addpresc(request, patient_id, appointment_id,):
    patient = Patient.objects.get(id=patient_id)
    appointment = Booking.objects.get(id=appointment_id)
    doctors = Doctor.objects.filter(id=request.session['doctor'])
    if request.method == 'POST':
        d_id = request.session['doctor']
        bkdate = request.POST['bdate']
        prscption = request.POST['prescribtion']
        b_id = request.session['booking']

        doc = Doctor.objects.get(id=d_id)

        addprescription = Description(patient = patient, Booking_id = b_id, discription_date = bkdate,
                                     description = prscption , doctor = doc,)
        addprescription.save()
        appointment.status = True
        appointment.save()
        
        request.session['prescription'] = addprescription.id
        print(doc)
        return redirect('doctor:appoin')
    return render(request, 'pages/addprescription.html', {'patient': patient, 'appointment': appointment,'doct':doctors})


def doc_profile(request):
    msg = ''
    doctdata = Doctor.objects.get(id = request.session['doctor'])

    if request.method=='POST':
        doctor = Doctor.objects.get(id = request.session['doctor'])

        pname = request.POST['p_name']
        pemail = request.POST['p_email']
        paddress = request.POST['p_address']
        phone_number = request.POST['p_number']
        pgender = request.POST['p_gender']
        dob = request.POST['dob']

        doctor.doc_name = pname
        doctor.doc_email = pemail
        doctor.doc_address = paddress
        doctor.doc_phone = phone_number
        doctor.doc_gender = pgender
        doctor.doc_dob = dob
        
        doctor.save()

        msg = 'Profile updated successfully'
        return redirect('doctor:dhome')

    return render(request,'pages/profile.html',{'doctdata':doctdata})

def doc_viewpat(request):
    patients = Description.objects.filter(doctor = request.session['doctor'])

    return render(request,'pages/viewpatient.html',{'patients':patients})

def passwordchange(request):
    msg=""
    doc_data = Doctor.objects.get(id=request.session['doctor'])
    if request.method == 'POST':
        doctor = Doctor.objects.get(id = request.session['doctor'])

        current_pass = request.POST['current_pass'] 
        new_pass = request.POST['new_pass'] 
        confirm_pass = request.POST['confirm_pass']

        if doctor.doc_pass == current_pass:

            if new_pass == confirm_pass:
                 doctor.doc_pass = new_pass
                 doctor.save()
                 msg = 'Password changed succesfully'

            else:
                msg = 'Password does not match'

        else:
            msg = 'Incorrect Password'
    context =  {'msg':msg,
                'data': doc_data,
                }
    return render(request,'pages/changepass.html',context)

def doc_logout(request):
    del request.session['doctor']
    request.session.flush() 
    return redirect('common:home')