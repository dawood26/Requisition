from django.shortcuts import render,redirect
from . import forms

from django.contrib.auth import authenticate,login
# Create your views here.

def index(request):

    return render(request,'department/home.html')

def signup(request):

    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
    else:

        form = forms.CustomUserCreationForm

    context= {'form': forms.CustomUserCreationForm}
    return render(request,'registration/signup.html',context)