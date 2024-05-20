from django.shortcuts import render, get_object_or_404
from auth_app.models import Patient, CustomUser, Doctor, FamilyDoctor
from cards_app.models import MedCards
from django.shortcuts import render, get_object_or_404
from auth_app.models import Patient, Doctor

def all_cards(request):
    user = request.user
    doctor = get_object_or_404(Doctor, user=user)
    patient = Patient.objects.select_related('user').prefetch_related('medcards', 'id_doctor').all()
    
    card_active_redact = Patient.objects.select_related('user').filter(id_doctor=doctor)
    
    user_groups = request.user.groups.values_list('name', flat=True)
    context = {
        'user_groups': list(user_groups),
        'patient': patient,
        'user': request.user,
        'doctor': doctor,
        'card_active_redact': card_active_redact,
    }
    return render(request, 'cards_app/all_cards.html', context)

