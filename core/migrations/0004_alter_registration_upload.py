# Generated by Django 5.1.4 on 2025-01-10 01:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_registration_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='upload',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='certificates'),
        ),
    ]
