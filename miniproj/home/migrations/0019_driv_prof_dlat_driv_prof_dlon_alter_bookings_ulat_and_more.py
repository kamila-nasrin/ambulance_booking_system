# Generated by Django 4.2.7 on 2023-12-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_bookings_lat_remove_bookings_lon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driv_prof',
            name='dlat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='driv_prof',
            name='dlon',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='ulat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='ulon',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='driv_loc',
            name='dlat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driv_loc',
            name='dlon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]