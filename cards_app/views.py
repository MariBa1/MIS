import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from auth_app.models import Patient,  Doctor
from cards_app.forms import CardVaccineForm, MedCardsForm
from cards_app.models import CardVaccine, IndividualMarks, MedCards



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
def not_card(request):
    return render(request, 'cards_app/not_card.html')

################ Пацієнти ##############

@login_required
def card_profile(request):
    user = request.user
    try:
        patient = get_object_or_404(Patient, user=user)
        card = get_object_or_404(MedCards.objects.select_related('patient', 
                                            'patient__user', 'doctor', 'doctor__user').prefetch_related('individualmarks_set'),patient=patient)
        individual_marks = IndividualMarks.objects.filter(medcard=card)
        context = {
                'user': user,
                'patient': patient,
                'card': card,
                'individual_marks':individual_marks,
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






@login_required
def index(request, card_id):
    card = get_object_or_404(MedCards.objects.select_related('patient', 
                                            'patient__user', 'doctor', 'doctor__user').prefetch_related('individualmarks_set'),  id=card_id)
    individual_marks = IndividualMarks.objects.filter(medcard=card)
    current_user = request.user
    doctor = card.doctor.user if card.doctor else None
    can_edit = doctor == current_user

    if request.method == 'POST':
        form = MedCardsForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('cards_app:index', card_id=card.id)
    else:
        form = MedCardsForm(instance=card)
    context = {
        'card': card,
        'can_edit': can_edit,
        'individual_marks': individual_marks,
        'form': form,
    }
    
    return render(request, 'cards_app/index.html', context)

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
def add_vaccine(request, card_id):
    card = get_object_or_404(MedCards, id=card_id)

    if request.method == 'POST':
        form = CardVaccineForm(request.POST)
        if form.is_valid():
            card_vaccine = form.save(commit=False)
            card_vaccine.medcard = card  # Присвоюємо медичну карту
            card_vaccine.save()
            return HttpResponseRedirect(reverse('cards_app:vaccine', args=[card.id]))  # Перенаправлення після успішного збереження
    else:
        form = CardVaccineForm()

    return render(request, 'cards_app/add_vaccine.html', {'form': form, 'card': card})



@login_required
def delete_vaccine(request, card_id):
    card = get_object_or_404(MedCards, id=card_id)
    if request.method == 'POST':
        logging.info(f"POST request received for card ID: {card_id}")
        vaccination_ids = request.POST.getlist('vaccination_ids')
        if vaccination_ids:
            logging.info(f"Deleting vaccinations with IDs: {vaccination_ids}")
            CardVaccine.objects.filter(id__in=vaccination_ids, medcard=card).delete()
        else:
            logging.info("No vaccination IDs to delete")
        return HttpResponseRedirect(reverse('cards_app:vaccine', args=[card.id]))
    else:
        logging.info("Request method is not POST")
    
    return redirect('cards_app:vaccine', card_id=card.id)