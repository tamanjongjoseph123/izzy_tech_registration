# Generated by Django 4.2.11 on 2025-01-07 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='upload',
            field=models.ImageField(upload_to='certificates/'),
        ),
    ]