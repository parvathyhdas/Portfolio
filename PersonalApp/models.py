from django.db import models

# Create your models here.
class contactdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=500,null=True,blank=True)
