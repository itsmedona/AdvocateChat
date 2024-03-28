
from django.db import models
from django.db.models.deletion import CASCADE

from Admin_app.models import Lawsdb
from Advocate_app.models import Advocatedb



# Create your models here.
class Userdb(models.Model):
    usrname = models.CharField(max_length=20,default='')
    mobilenumber  = models.IntegerField()
    emailid = models.CharField(max_length=20,default='')
    district = models.CharField(max_length=20,default='')
    image = models.ImageField(upload_to='Image',default='null.jpg')
    username = models.CharField(max_length=20,default='')
    password = models.CharField(max_length=20,default='')
    status = models.IntegerField(default=0)

class BookAdvocatedb(models.Model):
    userid = models.ForeignKey(Userdb,on_delete=CASCADE,null=True,blank=False)
    advocateid = models.ForeignKey(Advocatedb,on_delete=CASCADE,null=True,blank=False)
    image = models.ImageField(upload_to='Image',default='null.jpg')
    query = models.CharField(max_length=50,default='')
    status = models.IntegerField(default=0)
    update = models.CharField(max_length=50,default='Not Viewed by advocate')
    Room = models.CharField(max_length=50,default='')

