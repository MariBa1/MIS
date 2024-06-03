from .models import CardVaccine, Vaccination, MedCards
from django import forms 
from django.core.validators import MinLengthValidator
from datetime import date, timedelta
from django.utils import timezone

class CardVaccineForm(forms.ModelForm):
    class Meta:
        model = CardVaccine
        fields = ['vaccination','product_series','reaction','contraindication','date_vaccine']


    vaccination = forms.ModelChoiceField(queryset=Vaccination.objects.all())
    contraindication = forms.CharField(widget=forms.Textarea())
    product_series = forms.CharField(validators=[MinLengthValidator(5)])
    date_vaccine = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    
    def clean_date_vaccine(self):
        value = self.cleaned_data.get("date_vaccine")
        today = date.today()
        years_ago = today - timedelta(days=365.25)
        if value and value < years_ago:
            raise forms.ValidationError(f'Дане поле не приймає дати, менші за {years_ago}')
        elif value and value > date.today():
            raise forms.ValidationError(f'Дане поле не приймає дати, більші за {date.today()}' )
        return value


class MedCardsForm(forms.ModelForm):
    def clean_deregistration_date(self):
        deregistration_date = self.cleaned_data.get("deregistration_date")
        registration_date = self.instance.registration_date

        if deregistration_date and deregistration_date > timezone.now():
            raise forms.ValidationError('Дата виписки не може бути в майбутньому.')
        if deregistration_date and deregistration_date < registration_date:
            raise forms.ValidationError('Дата виписки не може бути ранішою за дату реєстрації.')

        return deregistration_date
    class Meta:
        model = MedCards
        fields = ['deregistration_date']