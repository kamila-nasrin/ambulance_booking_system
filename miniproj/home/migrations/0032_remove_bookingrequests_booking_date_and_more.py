# Generated by Django 4.2.7 on 2023-12-13 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_rename_driver_name_bookingrequests_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingrequests',
            name='Booking_date',
        ),
        migrations.RemoveField(
            model_name='bookingrequests',
            name='first_name',
        ),
    ]