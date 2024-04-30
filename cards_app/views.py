from django.shortcuts import render


def all_cards(request):
    return render(request, 'cards_app/all_cards.html')

