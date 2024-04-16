from django.shortcuts import render

def login(request):
    return render(request, 'auth_app/login.html')

def reg(request):
    return render(request, 'auth_app/reg.html')

def logout(request):
    return render(request, 'auth_app/logout.html')

