from pyexpat import model
from django.db import models

# Create your models here.
class employs (models.Model):
    name = models.CharField(max_length=50)
    field =  models.CharField(max_length=50)
    salary = models.IntegerField()
    assets= models.CharField(max_length=50)
class students(models.Model):
    Name= models.CharField(max_length=50)
    Standard= models.IntegerField()
    Subject= models.CharField(max_length=50)
    Marks= models.IntegerField()
    sports= models.CharField(max_length=50)



