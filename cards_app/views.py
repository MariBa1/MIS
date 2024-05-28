from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
# from django.urls import reverse
# from auth_app.context_processors import user_groups
# from .forms import CardVaccineForm  # Ваші форми для роботи з вакцинаціями
from auth_app.context_processors import user_groups
from auth_app.models import Patient, CustomUser, Doctor, FamilyDoctor
from cards_app.models import CardVaccine, MedCards, Vaccination

@login_required
def all_cards(request):
    user = request.user
    doctor = get_object_or_404(Doctor, user=user)
    patients_with_cards = Patient.objects.select_related('user').prefetch_related('medcards').filter(medcards__isnull=False).distinct()
    card_active_redact = patients_with_cards.filter(id_doctor=doctor)
    user_groups = request.user.groups.values_list('name', flat=True)
    context = {
        'user_groups': list(user_groups),
        'patients_with_cards': patients_with_cards,
        'user': request.user,
        'doctor': doctor,
        'card_active_redact': card_active_redact,
    }
    return render(request, 'cards_app/all_cards.html', context)


@login_required
def card_profile(request):
    user = request.user
    try:
        patient = get_object_or_404(Patient, user=user)
        card = get_object_or_404(MedCards.objects.select_related('patient', 
                                            'patient__user', 'doctor', 'doctor__user'),patient=patient)
        context = {
                'user': user,
                'patient': patient,
                'card': card,
            }
        return render(request, 'cards_app/index.html', context)
    except Http404:
        return render(request, 'cards_app/not_card.html')


@login_required
def vaccine_profile(request):
    user = request.user
    try:
        patient = get_object_or_404(Patient, user=user)
        card = get_object_or_404(MedCards.objects.select_related('patient', 'patient__user'),patient=patient)
        card_vaccinations = CardVaccine.objects.filter(medcard=card)

        context = {
                'user': user,
                'patient': patient,
                'card': card,
                'card_vaccinations': card_vaccinations,

            }
        return render(request, 'cards_app/vaccine.html', context)
    except Http404:
        return render(request, 'cards_app/not_card.html')



# def vaccine(request, card_id):
#     card = get_object_or_404(MedCards.objects.select_related('patient', 
#                                             'patient__user', 'doctor', 'doctor__user'),  id=card_id)
#     card_vaccinations = CardVaccine.objects.filter(medcard=card)
#     doctor = card.doctor.user
#     context = {
#         'card': card,
#         'doctor':doctor,
#         'card_vaccinations': card_vaccinations,
#     }
#     return render(request, 'cards_app/vaccine.html', context)
@login_required
def vaccine(request, card_id):
    card = get_object_or_404(MedCards.objects.select_related('patient', 'patient__user', 'doctor', 'doctor__user'), id=card_id)
    card_vaccinations = CardVaccine.objects.filter(medcard=card)
    current_user = request.user
    doctor = card.doctor.user if card.doctor else None
    can_edit = doctor == current_user  # Перевірка, чи є поточний користувач лікарем, прив'язаним до медичної картки

    context = {
        'card': card,
        'card_vaccinations': card_vaccinations,
        'can_edit': can_edit,  # Додаємо прапорець у контекст
    }
    
    return render(request, 'cards_app/vaccine.html', context)
@login_required
def examination_profile(request):
    user = request.user
    try:
        patient = get_object_or_404(Patient, user=user)
        card = get_object_or_404(MedCards.objects.select_related('patient', 
                                            'patient__user', 'doctor', 'doctor__user'),patient=patient)
        context = {
                'user': user,
                'patient': patient,
                'card': card,
            }
        return render(request, 'cards_app/examination.html', context)
    except Http404:
        return render(request, 'cards_app/not_card.html')
    

@login_required
def not_card(request):
    return render(request, 'cards_app/not_card.html')


@login_required
def index(request, card_id):
    card = get_object_or_404(MedCards.objects.select_related('patient', 
                                            'patient__user', 'doctor', 'doctor__user'),  id=card_id)
    context = {
        'card': card,
    }
    return render(request, 'cards_app/index.html', context)


@login_required
def examination(request, card_id):
    card = get_object_or_404(MedCards.objects.select_related('patient', 
                                            'patient__user', 'doctor', 'doctor__user'),  id=card_id)
    context = {
        'card': card,
    }
    return render(request, 'cards_app/examination.html', context)




