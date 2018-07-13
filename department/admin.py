from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import EmployeeUser, gender
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = EmployeeUser
    list_display = ['email', 'username','gender',]
admin.site.register(EmployeeUser,CustomUserAdmin)
