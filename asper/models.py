from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.FileField(null=True)
    phone = models.TextField(max_length=10, null=True)
    dept = models.TextField(max_length=20, null=True)

    def __str__(self):
        return self.usr.username

class FirstTask(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    Q1 = models.TextField(max_length=100, null=True)
    Q2 = models.TextField(max_length=100, null=True)
    Q3 = models.TextField(max_length=100, null=True)
    Q4 = models.TextField(max_length=100, null=True)
    Q5 = models.TextField(max_length=100, null=True)
    Q6 = models.TextField(max_length=100, null=True)
    Q7 = models.TextField(max_length=100, null=True)
    Q8 = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.usr.username

class Project(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    ProjectName = models.TextField(max_length=10, null=True)
    ProjectType = models.TextField(max_length=10, null=True)
    ProjectImg = models.FileField(null=True)

    def __str__(self):
        return self.usr.username