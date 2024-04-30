from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from auth_app.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  ##вводемо на перевірку словник з даними при вводі
        if form.is_valid(): ##якщо дані відповідають стандарту
            username = request.POST['username'] ## зі словника добуваєм username & password
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) ## чи є такий користувач??
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('cards_app:prof_doc'))
    else:
        form = UserLoginForm()    
    context = {
        'form': form
    }
    return render(request, 'auth_app/login.html',context)


def reg(request):
    return render(request, 'auth_app/reg.html')


def logout(request):
    return render(request, 'auth_app/logout.html')



def new_pass(request):
    return render(request, 'auth_app/new_pass.html')

def profile_doc(request):
    return render(request, 'auth_app/profile.html')

