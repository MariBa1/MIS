from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render, HttpResponseRedirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse
from auth_app.forms import ProfileForm, UserLoginForm, UserRegForm, PatientForm, DoctorForm, AddressForm
from auth_app.models import Patient, Doctor


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
def profile(request):
  user = request.user
  user_groups = user.groups.values_list('name', flat=True)

  if request.method == 'POST':
    form = ProfileForm(data=request.POST, instance=user, files=request.FILES)
    address_form = AddressForm(request.POST, instance=user.patient.address if hasattr(user,
                                                                                      'patient') and user.patient.address else None)

    patient_form = None
    doctor_form = None

    # Перевірка, чи користувач належить до групи ПАЦІЄНТИ
    if 'ПАЦІЄНТИ' in user_groups:
      patient_instance, created = Patient.objects.get_or_create(user=user)
      patient_form = PatientForm(request.POST, instance=patient_instance)

    # Перевірка, чи користувач належить до групи ЛІКАРІ
    if 'ЛІКАРІ' in user_groups:
      try:
        doctor_instance = Doctor.objects.get(user=user)
        doctor_form = DoctorForm(request.POST, instance=doctor_instance)
      except Doctor.DoesNotExist:
        doctor_form = None

    # Перевірка валідності форм та їх збереження
    if form.is_valid() and address_form.is_valid() and (patient_form is None or patient_form.is_valid()) and (
       doctor_form is None or doctor_form.is_valid()):
      form.save()
      if patient_form:
        address = address_form.save()
        patient = patient_form.save(commit=False)
        patient.address = address
        patient.save()
      if doctor_form:
        doctor_form.save()  # Збереження змін у існуючому записі лікаря
      return HttpResponseRedirect(reverse('auth_app:profile'))
  else:
    form = ProfileForm(instance=user)
    address_form = AddressForm(
      instance=user.patient.address if hasattr(user, 'patient') and user.patient.address else None)

    patient_form = None
    doctor_form = None

    # Перевірка, чи користувач належить до групи ПАЦІЄНТИ
    if 'ПАЦІЄНТИ' in user_groups:
      patient_instance, created = Patient.objects.get_or_create(user=user)
      patient_form = PatientForm(instance=patient_instance)

    # Перевірка, чи користувач належить до групи ЛІКАРІ
    if 'ЛІКАРІ' in user_groups:
      try:
        doctor_instance = Doctor.objects.get(user=user)
        doctor_form = DoctorForm(instance=doctor_instance)
      except Doctor.DoesNotExist:
        doctor_form = None

  context = {
    'form': form,
    'user_groups': list(user_groups),
    'patient_form': patient_form,
    'doctor_form': doctor_form,
    'address_form': address_form,
  }
  return render(request, 'auth_app/profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main_app:index'))


def new_pass(request):
    return render(request, 'auth_app/new_pass.html')


