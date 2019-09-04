from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.
def student_login(request):
    return render(request, 'studentbook/login.html', {})


def student_signup(request):
    return render(request, 'studentbook/signup.html', {})


def register_student(request):
    if request.POST:
        username = request.POST['student_name']
        email = request.POST['student_email']
        password = request.POST['student_password']

        obj = User(username=username, email=email, password=password)
        obj.set_password(password)
        obj.save()

        return render(request, 'studentbook/register_student.html', {})
    return redirect('studentbook:student_login')
