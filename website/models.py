from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Students(models.Model):
    name= models.CharField(max_length=200)
    college= models.CharField(max_length=200)
    age= models.IntegerField()
    isActive= models.BooleanField(default= False)
