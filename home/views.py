from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Departments,Doctors,Contact
from.forms import BookingForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import BookingForm
from datetime import date
# Create your views here.
def index(request):
    return render(request,'index.html',)

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            p_name=form.cleaned_data.get('p_name')
            email=form.cleaned_data.get('p_email')
            subject = 'City Hospital Appointment Request Received'
            message = f'Thank you Mr/Mrs.{p_name} for submitting your request for a hospital appointment. We have received your information and will process your request shortly.\n\nOur hospital help desk will reach out to you soon to confirm your appointment \n\nIf you have any urgent concerns or need immediate assistance, please contact us directly \nEmergency-Helpline:808080-3333.\n\nThank you for choosing our hospital!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )

            return render(request,'confirmation.html')
        else:
            form = BookingForm(initial={'booking_date': date.today()})

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def department(request):
    dict_dept={'dept':Departments.objects.all()
               }
    return render(request,'department.html',dict_dept)

def contact(request):
    return render(request,'contact.html')

def contact(request):
    if request.method=="POST":
        contact=Contact()
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

    
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        
        return render(request,'contact_confirmation.html')
    return render(request,'contact.html')

 