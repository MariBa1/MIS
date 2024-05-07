from django.shortcuts import render
from auth_app.models import Patient


def all_cards(request):
    patients = Patient.objects.all()
    return render(request, 'cards_app/all_cards.html', {'patients': patients})

