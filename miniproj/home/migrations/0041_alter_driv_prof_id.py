# Generated by Django 4.2.7 on 2023-12-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_delete_bookingrequests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driv_prof',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]