from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from auth_app.models import CustomUser

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model = CustomUser