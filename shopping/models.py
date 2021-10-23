from django.db import models
class Category(models.Model):
    name =  models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subname = models.CharField(max_length= 200)
    def __str__(self):
        return self.subname + '--' + self.category.name

class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    proname =  models.CharField(max_length=200)
    proprice =  models.FloatField()
    prodescription =  models.TextField()
    prodiscount =  models.CharField(max_length=20)
    prospecification = models.TextField()
    proimage = models.FileField(null=True)
    proimage2 = models.FileField(null=True)
    proimage3 = models.FileField(null=True)
    proimage4 = models.FileField(null=True)

    def __str__(self):
        return self.proname + '--' + self.subcategory.subname
