from django.shortcuts import render,redirect
from .models import Team
from carss.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured_cars=Car.objects.order_by("-created_date").filter(is_featured=True)    
    all_cars=Car.objects.order_by("-created_date")
    model_search=Car.objects.values_list('model',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    data={
        'featured_cars':featured_cars,
        'teams':teams,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request,'pages/home.html',data)

def about(request):
    teams=Team.objects.all()
    data={
        'teams':teams,
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    if request.method=='POST':
        messages.success(request,"Thank You for contacting us.")
        return redirect('contact')
    return render(request,'pages/contact.html')