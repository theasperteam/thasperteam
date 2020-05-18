from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.FileField(null=True)
    phone = models.TextField(max_length=10, null=True)
    dept = models.TextField(max_length=20, null=True)
    FirstN = models.TextField(max_length=100, null=True)
    LastN = models.TextField(max_length=100, null=True)
    EmailA = models.TextField(max_length=70, null=True)
    JoinDate = models.DateField(null=True)

    def __str__(self):
        return self.usr.username

class UserSkills(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Skills = models.TextField(max_length=30, null=True)

    def __str__(self):
        return self.usr.username

class UserPort(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    FirstN = models.TextField(max_length=100, null=True)
    LastN = models.TextField(max_length=100, null=True)
    LinkedIn = models.TextField(max_length=100, null=True)
    Behance = models.TextField(max_length=100, null=True)
    Instagram = models.TextField(max_length=100, null=True)
    Twitter = models.TextField(max_length=100, null=True)
    Github = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.usr.username


class FirstTask(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    FirstTS = models.DateField(null=True)
    ud = models.TextField(max_length=100, null=True)
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
    ProjectPosted = models.DateField(null=True)

    def __str__(self):
        return self.usr.username



class DesignAssignment(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    AssigmentNo = models.CharField(max_length=5, null=True)
    AssignmentDis = models.TextField(max_length=50, null=True)
    Todo = models.TextField(max_length=100, null=True)


    def __str__(self):
        return self.AssigmentNo


class DesignSubmit(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    AssignNo = models.ForeignKey(DesignAssignment, on_delete=models.CASCADE, null=True)
    Assignmentimng = models.FileField(null=True)
    Status = models.BooleanField(null=True)

    def __self__(self):
        return self.AssigmentNo



class WebAssignment(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    AssigmentNo = models.TextField(max_length=5, null=True)
    AssignmentDis = models.TextField(max_length=50, null=True)
    Todo = models.TextField(max_length=100, null=True)


    def __str__(self):
        return self.AssigmentNo

class WebSubmit(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    AssignNo = models.ForeignKey(WebAssignment, on_delete=models.CASCADE, null=True)
    Assignmentimng = models.FileField(null=True)
    Status = models.BooleanField(null=True)

    def __self__(self):
        return self.usr.AssigmentNo

class AppAssignment(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    AssigmentNo = models.TextField(max_length=5, null=True)
    AssignmentDis = models.TextField(max_length=50, null=True)
    Todo = models.TextField(max_length=100, null=True)


    def __str__(self):
        return self.AssigmentNo

class AppSubmit(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    AssignNo = models.ForeignKey(AppAssignment, on_delete=models.CASCADE, null=True)
    Assignmentimng = models.FileField(null=True)
    Status = models.BooleanField(null=True)

    def __self__(self):
        return self.usr.AssigmentNo

