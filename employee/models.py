from django.db import models
from django.forms import CharField

# Create your models here.
class Emp(models.Model):
    name= models.CharField(max_length=200)
    emp_id= models.CharField(max_length=20)
    phone= models.CharField(max_length=10)
    address= models.CharField(max_length=150)
    working= models.BooleanField(default= True)
    department= models.CharField(max_length=11)
    
    
    
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name= models.CharField(max_length=200)
    testimonial= models.TextField()
    picture= models.ImageField(upload_to= "testimonials/")
    rating= models.IntegerField()

    def __str__(self):
        return self.testimonial
