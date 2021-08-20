from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('register', register, name = 'student_register'),
    path('login', login, name="student_login"),
    path('dashboard', dashboard, name="student_dashboard"),
    path('get_student/<ustudent>', get_student, name="get_student"),
    path('delete', delete, name="delete_student")
]