from django.shortcuts import render


# Create your views here.
def student_login(request):
    return render(request, 'studentbook/login.html', {})


def student_signup(request):
    return render(request, 'studentbook/signup.html', {})
