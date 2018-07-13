from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import EmployeeUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = EmployeeUser
        fields = ('username', 'email','emp_phone','gender')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = EmployeeUser
        fields = ('username', 'email','emp_phone','gender')

