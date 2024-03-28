
from django.db import models

# Create your models here.
class Advocatedb(models.Model):
    adname = models.CharField(max_length=20,default='')
    mobilenumber  = models.IntegerField()
    emailid = models.CharField(max_length=20,default='')
    advocatetype = models.CharField(max_length=20,default='')
    district = models.CharField(max_length=20,default='')
    image = models.ImageField(upload_to='Image',default='null.jpg')
    username = models.CharField(max_length=20,default='')
    password = models.CharField(max_length=20,default='')
    status = models.IntegerField(default=0)
