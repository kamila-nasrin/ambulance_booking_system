from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from geopy.distance import geodesic
# Create your views here

def loginPage(request):
    if request.method == 'POST':
        usrname = request.POST.get('username')
        passwd = request.POST.get('pass3')
        user = authenticate(request, username=usrname, password=passwd)
        if user is not None:
            login(request, user)
            messages.info(request, f'{usrname}, You are logged in')
            return redirect('driv_prof')
        else:
            messages.info(request, 'Invalid Username or Password')

    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def drivers(request):
    return render(request, 'drivers.html')

@login_required(login_url='login')
def drivereg(request):
    if request.method == 'POST':
        form = Driv_profForm(request.POST, request.FILES, instance=request.user.driv_prof)
        if form.is_valid():
            form.save()

            # Render driv_prof.html with the updated data
            return render(request, 'driv_prof.html', {'form': form})
        else:
            messages.error(request, 'Form is not valid. Please check the errors.')
    else:
        form = Driv_profForm(instance=request.user.driv_prof)

    return render(request, 'drivereg.html', {'form': form})


@login_required(login_url='login')
def driv_prof(request):
    user_driv_prof = request.user.driv_prof

    if request.method == 'POST':
        form = Driv_profForm(request.POST, request.FILES, instance=user_driv_prof)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Form is not valid. Please check the errors.')
    else:
        form = Driv_profForm(instance=user_driv_prof)

    return render(request, 'driv_prof.html', {'form': form})
    
def hospitals(request):
    dict_hosp={
        'hosp': Hospitals.objects.all()
    }
    return render(request,'hospitals.html', dict_hosp)

def signup(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Your account is created')
            return redirect('login')
        else:
            context={'form':form}  
            messages.info(request,'Invalid Credentials')  
            return render(request, 'signup.html',context)
    context={'form':form}    
    return render(request, 'signup.html',context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You have logged out successfully')
    return redirect('login')

def booking_form(request):
    if request.method == 'POST':
        form = BookingsForm(request.POST)
        if form.is_valid():
            form.save()
            # Get the user's location
        user_latitude = '11.12'           
        user_longitude = '76.13'
        user_location = (user_latitude, user_longitude)
            # Sort drivers by distance
        drivers = Driv_prof.objects.all()
        sorted_drivers = sorted(drivers, key=lambda x: geodesic(user_location, (x.latitude, x.longitude)))

        usr_dict = {
            'usrs': sorted_drivers
        }            
        return render(request, 'drivers.html', usr_dict)

        # Handle form validation errors

    else:
        form = BookingsForm()

    context = {'form': form}
    return render(request, 'booking_form.html', context)
