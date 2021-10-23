from django.db import models
class college(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length= 30)
    contact = models.IntegerField()
class contact(models.Model):
    email = models.CharField(max_length=50)
    pin = models.CharField(max_length= 30)
    contact = models.IntegerField()
    image = models.CharField(max_length=300,null=True)