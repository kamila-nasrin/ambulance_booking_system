# Generated by Django 4.2.7 on 2023-12-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_driv_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='latitude',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='bookings',
            name='longitude',
            field=models.FloatField(default='0'),
        ),
        migrations.DeleteModel(
            name='Driv_Loc',
        ),
    ]
