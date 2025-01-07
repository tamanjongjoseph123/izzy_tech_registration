from django.db import models

# Create your models here.
class Registration(models.Model):
    full_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    nic = models.CharField(max_length=20)
    certificate = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    upload = models.ImageField(upload_to='certificates/')
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
