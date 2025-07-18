from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Roll_no=models.CharField(max_length=100)
    marks=models.CharField(max_length=100)
    photo=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100)


