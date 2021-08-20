from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ("fn", "ln", "uname", "password", "coo")

admin.site.register(Student, StudentAdmin)
# Register your models here.
