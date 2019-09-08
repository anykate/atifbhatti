from django.urls import path
from . import views


app_name = 'studentbook'

urlpatterns = [
    path('', views.student_login, name='student_login'),
    path('home/', views.student_home, name='student_home'),
    path('signup/', views.student_signup, name='student_signup'),
    path('register/', views.register_student, name='register_student'),
    path('logout/', views.student_logout, name='student_logout'),
]
