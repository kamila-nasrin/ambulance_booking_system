# Generated by Django 4.2.7 on 2023-12-06 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_location_remove_bookings_ulat_remove_bookings_ulon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driv_prof',
            name='dlat',
        ),
        migrations.RemoveField(
            model_name='driv_prof',
            name='dlon',
        ),
        migrations.DeleteModel(
            name='Driv_loc',
        ),
    ]
