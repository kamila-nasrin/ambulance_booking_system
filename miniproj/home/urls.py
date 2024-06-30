from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drivers', views.drivers, name='drivers'),
    path('login/', views.loginPage, name='login'),
    path('hospitals', views.hospitals, name='hospitals'),
    path('drivereg', views.drivereg, name='drivereg'),
    path('signup', views.signup, name='signup'),
    path('driv_prof', views.driv_prof, name='driv_prof'),
    path('booking_form', views.booking_form, name='booking_form'),
    ]