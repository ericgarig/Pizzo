from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=8)
    state_start = models.DateField()

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()


class Employee(models.Model):
    ssn = models.CharField(max_length=9, unique=True)
    name_last = models.CharField(max_length=255)
    name_first = models.CharField(max_length=225)
    name_nick = models.CharField(max_length=255)
    date_birth = models.DateField()
    date_hire = models.DateField()
    rate_hourly = models.FloatField()
    rate_Increate_date = models.DateField()
    address_Street = models.CharField(max_length=255)
    address_City = models.CharField(max_length=255)
    address_State = models.CharField(max_length=2)
    address_Zip = models.CharField(max_length=5)
    phone_cell = models.CharField(max_length=10)
    phone_home = models.CharField(max_length=10)
    isPancho = models.BooleanField(default=0)
    isTempLayoff = models.BooleanField(default=0)
    
    def __str__(self):
        return self.name_last & ', ' & self.name_first


class Attendance(models.Model):
    employee_id = models.ForeignKey(Employee)
    project_id = models.ForeignKey(Project)
    date = models.DateField()
    hours = models.FloatField(default=8)
    cost_per_day = models.FloatField()