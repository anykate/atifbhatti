from django.urls import path
from . import views


app_name = 'studentbook'

urlpatterns = [
    path('', views.student_login, name='student_login'),
    path('signup/', views.student_signup, name='student_signup'),
]
