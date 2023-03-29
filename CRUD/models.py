from django.db import models

class Students(models.Model):
    Name=models.CharField(max_length=100,blank=False,null=False)
    Email=models.EmailField()
    Age=models.IntegerField()
    Gender=models.CharField(max_length=100,blank=False,null=False)