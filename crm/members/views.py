from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have successfully logged in!")
            return redirect('index')
        
        else:
            messages.success(request,'some error')
            return render(request, 'members/login.html',)
    return render(request, 'members/login.html')

def user_logout(request):
    logout(request)
    messages.success(request,"You have successfully logged out.")
    return redirect('user_login')

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #after sign up, logg them in
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Your account has been created successfully")
            return redirect('index')
        
        
    return render(request,'members/signup.html', {'form': form})