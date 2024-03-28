from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Lawsdb(models.Model):
    lawtype = models.CharField(max_length=20)
    lawname = models.CharField(max_length=20)
    lawdescription = models.CharField(max_length=1000)

class Law(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

class IPCSections(models.Model):
    type = models.ForeignKey(Law,on_delete=CASCADE,null=True,blank=False)
    ipcsection = models.CharField(max_length=20)
    ipcdescription = models.CharField(max_length=100)