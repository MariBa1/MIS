from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from auth_app.models import CustomUser, Patient
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import MinValueValidator

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = CustomUser


class UserRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","username",
              "email", "phone_number","password1", "password2",)
    
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

    # city = forms.CharField(required=False)
    # village = forms.CharField(required=False)
    # street = forms.CharField(required=False)
    # house = forms.IntegerField(required=False, validators=[MinValueValidator(1)])
    # apartment = forms.IntegerField(required=False, validators=[MinValueValidator(1)])

    # date_of_birth = forms.DateField()
    # sex = forms.ChoiceField()

    # specialization = forms.CharField()
    # stazh = forms.CharField()
    # Umovy_pryyomu = forms.CharField(required=False)
