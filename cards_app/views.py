from django.shortcuts import render
from auth_app.models import Patient


def all_cards(request):
  user_groups = request.user.groups.values_list('name', flat=True)
  context = {
    'user_groups': list(user_groups),
  }
  return render(request, 'cards_app/all_cards.html', context)

