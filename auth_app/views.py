from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from auth_app.forms import UserLoginForm, UserCreationForm, UserRegForm
from auth_app.models import CustomUser


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  ##вводемо на перевірку словник з даними при вводі
        if form.is_valid(): ##якщо дані відповідають стандарту
            username = request.POST['username'] ## зі словника добуваєм username & password
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) ## чи є такий користувач??
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('auth_app:prof_doc'))
    else:
        form = UserLoginForm()    
    context = {'form': form}
    return render(request, 'auth_app/login.html',context)


def reg(request):
    if request.method == 'POST':
        form = UserRegForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('auth_app:prof_doc'))
    else:
        form = UserRegForm()
    context = {'form': form}
    return render(request, 'auth_app/reg.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main_app:index'))



def new_pass(request):
    return render(request, 'auth_app/new_pass.html')

def profile_doc(request):
    return render(request, 'auth_app/profile.html')

