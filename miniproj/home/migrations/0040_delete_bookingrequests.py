# Generated by Django 4.2.7 on 2023-12-13 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_rename_location_hospitals_place_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookingRequests',
        ),
    ]
