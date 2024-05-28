from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from auth_app.models import CustomUser, Patient, Doctor
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import MinValueValidator
from .models import FamilyDoctor
from datetime import date, timedelta


class FamilyDoctorForm(forms.ModelForm):
  class Meta:
    model = FamilyDoctor
    fields = '__all__'

  def clean(self):
    cleaned_data = super().clean()
    patient = cleaned_data.get("patient")
    doctor = cleaned_data.get("doctor")

    if self.instance.pk:
      # Якщо запис вже існує, виключити його з перевірки
      if FamilyDoctor.objects.filter(patient=patient).exclude(pk=self.instance.pk).exists():
        raise forms.ValidationError("Цей пацієнт вже має сімейного лікаря")
    else:
      # Якщо запис новий, виконати стандартну перевірку
      if FamilyDoctor.objects.filter(patient=patient).exists():
        raise forms.ValidationError("Цей пацієнт вже має сімейного лікаря")

    return cleaned_data


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = CustomUser


class UserRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username",
                  "email", "phone_number", "password1", "password2",)

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput())


class ProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("img", "first_name", "last_name",
                  "patronymic", "email", "phone_number",
                  )

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("date_of_birth", "sex")
        date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    def clean_date_of_birth(self):
        value = self.cleaned_data.get("date_of_birth")
        today = date.today()
        eighty_years_ago = today - timedelta(days=80*365.25)
        if value and value < eighty_years_ago:
            raise forms.ValidationError(f'Дане поле не приймає дати, менші за {eighty_years_ago}')
        elif value and value> date.today():
            raise forms.ValidationError(f'Дане поле не приймає дати, більші за {date.today()}' )
        return value
    # def __init__(self,*args, **kwargs):
    #    super(PatientForm,self).__init__(*args, **kwargs)
    #    self.fields['user'].queryset = CustomUser.objects.exclude(groups__name__in=["ПАЦІЄНТИ","ЛІКАРІ"]).exclude(is_staff=True)

class DoctorForm(forms.ModelForm):
  class Meta:
    model = Doctor
    fields = ("specialization", "stazh", "Umovy_pryyomu")

