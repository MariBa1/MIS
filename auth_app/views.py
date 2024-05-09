from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from auth_app.forms import ProfileForm, UserLoginForm, UserCreationForm, UserRegForm
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

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('auth_app:profile'))
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
            return HttpResponseRedirect(reverse('auth_app:profile'))
    else:
        form = UserRegForm()
    context = {'form': form}
    return render(request, 'auth_app/reg.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main_app:index'))



def new_pass(request):
    return render(request, 'auth_app/new_pass.html')
    


@login_required
def profile(request):
    if request.method == 'POST':
        # data = request.POST.get('data_field')
        form = ProfileForm(data=request.POST, instance = request.user, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth_app:profile'))
    else:
        form = ProfileForm(instance = request.user)
    
    user_groups = request.user.groups.values_list('name', flat=True)
    context = {'form': form,
              'user_groups': list(user_groups), }
    return render(request, 'auth_app/profile.html', context)

