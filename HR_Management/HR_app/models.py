from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class EmployeeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empid = models.CharField(max_length=50)
    empdept = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=50, null=True)
    joiningdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username


class EmployeeEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coursepg = models.CharField(max_length=100, null=True)
    universitypg = models.CharField(max_length=200, null=True)
    pgraduationyr = models.CharField(max_length=20, null=True)
    percentagepg = models.CharField(max_length=30, null=True)
    coursegra = models.CharField(max_length=100, null=True)
    universitygra = models.CharField(max_length=200, null=True)
    graduationyr = models.CharField(max_length=20, null=True)
    percentagegr = models.CharField(max_length=30, null=True)
    coursessc = models.CharField(max_length=100, null=True)
    universityssc = models.CharField(max_length=200, null=True)
    graduationyrssc = models.CharField(max_length=20, null=True)
    percentagessc = models.CharField(max_length=30, null=True)
    coursehsc = models.CharField(max_length=100, null=True)
    universityhsc = models.CharField(max_length=200, null=True)
    graduationyrhsc = models.CharField(max_length=20, null=True)
    percentagehsc = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username

class LeaveRequests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empid = models.CharField(max_length=50, default='')
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')

    def _str_(self):
        return self.user.username
