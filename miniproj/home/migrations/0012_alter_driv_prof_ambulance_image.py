# Generated by Django 4.2.7 on 2023-12-05 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_driv_prof_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driv_prof',
            name='ambulance_image',
            field=models.ImageField(default='media/default.jpg', upload_to='media'),
        ),
    ]
