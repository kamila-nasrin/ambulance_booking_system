# Generated by Django 4.2.7 on 2023-12-06 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_driv_prof_lat_driv_prof_lon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driv_prof',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='driv_prof',
            name='lon',
        ),
    ]