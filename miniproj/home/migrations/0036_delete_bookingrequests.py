# Generated by Django 4.2.7 on 2023-12-13 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_alter_driv_prof_first_name_bookingrequests'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookingRequests',
        ),
    ]