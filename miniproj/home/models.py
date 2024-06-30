from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Hospitals(models.Model):
    hos_name=models.CharField(max_length=100)
    contact_info=models.CharField(max_length=50)
    location=models.TextField(max_length=100)
    hos_site=models.CharField(max_length=50)
    def __str__(self):
        return self.hos_name

class Driv_prof(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=30)
    description=models.CharField(default='My ambulance is registered under XYZ hospital or privately owned',max_length=200)
    place=models.CharField(max_length=100)
    phone_num=models.CharField(max_length=20)
    alternate_phone_number=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    vehicle_num=models.CharField(max_length=30)
    amb_type=models.CharField(max_length=100)
    amb_status=models.CharField(max_length=100)
    ambulance_image=models.ImageField(default='media/ambu.png',upload_to='media')
    latitude=models.FloatField(blank=True, null=True)
    longitude=models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.first_name

class Bookings(models.Model):
    Name=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Phone_number=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name

class BookingRequests(models.Model):
    Name=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Phone_number=models.CharField(max_length=100)
    phone_num=models.ForeignKey(Driv_prof, on_delete=models.CASCADE)
    booking_date=models.DateField(auto_now_add=True)