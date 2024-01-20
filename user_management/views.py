from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('list_blog')
        else:
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def user_logout(request):
    logout(request)
    return redirect('list_blog')