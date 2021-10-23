from django.db import models
class college(models.Model):
    name=models.CharField(max_length=30)
    collegeid=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    contact=models.IntegerField()
    def __str__(self):
        return self.name

class students(models.Model):
    clg=models.ForeignKey(college,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=20)
    rollno=models.CharField(max_length=15)
    email=models.CharField(max_length=40)
    number=models.IntegerField()
    image=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.name


class teachers(models.Model):
    clg = models.ForeignKey(college, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=20)
    teacherid=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    number=models.IntegerField()

    def __str__(self):
        return self.name




