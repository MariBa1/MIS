from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from auth_app.models import CustomUser, Patient, Doctor, Address
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import MinValueValidator
from .models import FamilyDoctor


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

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput())


class ProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("img", "first_name", "last_name",
                  "patronymic", "email", "phone_number",

                  # "city", "village", "street",
                  # "house", "apartment",
                  )

    img = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField(required=False)
    email = forms.CharField()
    phone_number = PhoneNumberField()


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("date_of_birth", "sex",)

        date_of_birth = forms.DateField(required=False)


class DoctorForm(forms.ModelForm):
  class Meta:
    model = Doctor
    fields = ("specialization", "stazh", "Umovy_pryyomu")


class AddressForm(forms.ModelForm):
  class Meta:
    model = Address
    fields =("city", "village", "street", "house", "apartment")
    city = forms.CharField(required=False)
    village = forms.CharField(required=False)
    street = forms.CharField(required=False)
    house = forms.IntegerField(required=False, validators=[MinValueValidator(1)])
    apartment = forms.IntegerField(required=False, validators=[MinValueValidator(1)])

