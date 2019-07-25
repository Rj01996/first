from django.shortcuts import render
from .forms import Student, EmployeeForm,TeacherForm

# Create your views here.
def form(request):
	stu = Student()
	return render(request, 'form.html',{'form':stu,"name":"Demo User"})

def empform(request):
	emp = EmployeeForm()	
	return render(request, 'form.html', {'form':emp})

def TeachForm(request):
	teach =TeacherForm()
	return render(request, 'techform.html', {'form':teach})