from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User
from django.core.mail import send_mail
# Create your views here.

def inquiry(request):
    if request.method=='POST':
        car_id=request.POST['car_id']
        car_title=request.POST['car_title']
        user_id=request.POST['user_id']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        customer_need=request.POST['customer_need']
        city=request.POST['city']
        state=request.POST['state']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already submitted a request for this car, please wait for further communication.')
                return redirect('/cars/'+car_id)        
        contact=Contact(car_id=car_id,car_title=car_title,user_id=user_id,first_name=first_name,last_name=last_name,customer_need=customer_need,city=city,state=state,email=email,phone=phone,message=message)
        contact.save()
        messages.success(request,'Your request has been submitted, we will get back with you shortly.')
        return redirect('/cars/'+car_id) 