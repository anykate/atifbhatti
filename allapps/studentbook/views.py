from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.
def student_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        student = authenticate(request, username=username, password=password)
        if student:
            messages.success(
                request, f'User \"{username}\" authenticated successfully!')
            return redirect('studentbook:student_home')

        else:
            messages.error(request, 'Invalid user credentials!')
    return render(request, 'studentbook/login.html', {})


def student_signup(request):
    return render(request, 'studentbook/signup.html', {})


def register_student(request):
    if request.POST:
        username = request.POST['student_name']
        email = request.POST['student_email']
        password = request.POST['student_password']

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            messages.error(request, 'Username / Email Address must be unique!')

        else:
            obj = User(username=username, email=email, password=password)
            obj.set_password(password)
            obj.save()

            messages.success(
                request, f'User \"{username}\" created successfully!')

    return redirect('studentbook:student_login')


def student_home(request):
    return render(request, 'studentbook/home.html', {})
