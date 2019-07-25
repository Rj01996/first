from django import forms
from .models import Employee,TeacherDetails

class Student(forms.Form):
	name = forms.CharField(max_length=50)
	age = forms.IntegerField()
	address = forms.CharField()


class EmployeeForm(forms.ModelForm):
	class Meta: 
		model = Employee
		fields = "__all__"
		# fields = ['name','age']

class TeacherForm(forms.ModelForm):
	class Meta:
		model = TeacherDetails
		fields = "__all__"
		

