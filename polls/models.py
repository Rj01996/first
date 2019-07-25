from django.db import models


class Employee(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	address = models.TextField()
	dept = models.CharField(max_length=50)



class TeacherDetails(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	mobile_no = models.IntegerField()