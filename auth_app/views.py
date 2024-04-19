from django.shortcuts import render

def login(request):
    return render(request, 'auth_app/login.html')

def reg(request):
    return render(request, 'auth_app/reg.html')

def logout(request):
    return render(request, 'auth_app/logout.html')

def profile_pat(request):
    return render(request, 'auth_app/prof_pat.html')

def profile_doc(request):
    return render(request, 'auth_app/prof_doc.html')

