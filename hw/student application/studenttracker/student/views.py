from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import *
# Create your views here.
def index(request):
	request.session['user'] = False
	return render(request, 'index.jinja')

def register(request):
	context = {}
	if (request.method == "POST"):
		fn = request.POST['fn']
		ln = request.POST['ln']
		uname = request.POST['uname']
		password = request.POST['password']
		coo = request.POST['coo']
		if (not Student.objects.filter(uname=uname)):
			stu = Student(fn=fn, ln=ln, uname=uname, password=password, coo=coo)
			stu.save()
			request.session['user'] = uname
			return redirect('student_dashboard')
		else:
			context['message'] = "Username in database."
	return render(request, 'register.jinja', context)

def login(request):
	context = {}
	if (request.method == "POST"):
		uname = request.POST['uname']
		password = request.POST['password']
		uver=Student.objects.filter(uname=uname)
		if (uver):
			uver = uver[0]
			if (uver.password == password):
				request.session['user'] = uname
				return redirect('student_dashboard')
			else:
				context['message'] = "Incorrect Password."
		else:
			context['message'] = "User not in database."
	return render(request, 'login.jinja', context)

def dashboard(request):
	context = {}
	if (request.session['user']):
		context['students'] = list(Student.objects.all())
		return render(request, 'dashboard.jinja', context)
	return redirect('index')

def get_student(request, ustudent):
	if (request.session['user']):
		student = Student.objects.filter(uname=ustudent)
		if (student):
			student = student[0]
			context = {'student':student}
			context['edit'] = False
			prev = [["first name: ", student.fn], ["last name: ", student.ln], 
			["username: ", student.uname], ["password: ", student.password], 
			["COO: ", student.coo]]
			context['prev'] = prev
			nopass = [["first name: ", student.fn], ["last name: ", student.ln], 
			["username: ", student.uname], ["password: ", "******"], 
			["COO: ", student.coo]]
			context['nopass'] = nopass
			if (request.session['user'] == ustudent):
				context['edit'] = True
			if (request.method == "POST"):
				fn = request.POST['fn']
				ln = request.POST['ln']
				uname = request.POST['uname']
				password = request.POST['password']
				coo = request.POST['coo']
				if (uname == student.uname or not Student.objects.filter(uname=uname)):
					curr = [fn, ln, uname, password, coo]
					for i in range(len(curr)):
						if (curr[i] == ""):
							curr[i] = prev[i]
					student.fn = curr[0]
					student.ln = curr[1]
					student.uname = curr[2]
					student.password = curr[3]
					student.coo = curr[4]
					student.save()
					request.session['user'] = student.uname
					return redirect('get_student', ustudent=student.uname)
			return render(request, 'get_student.jinja', context)
	return redirect('index')
def delete(request):
	Student.objects.filter(uname=request.session['user']).delete()
	request.session['user'] = False
	return redirect('index')
def get_country(request, country):
	context = {}
	if (request.session['user']):
		coo = Student.objects.filter(coo=country)
		if (coo):
			context['country'] = country
			context['pefrom'] = list(coo)
			return render(request, 'get_country.jinja', context)
	return redirect('index')