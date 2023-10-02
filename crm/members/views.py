from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages

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