from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from auth_app.models import CustomUser

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