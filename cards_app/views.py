from django.shortcuts import render

def index(request):
    return render(request, 'cards_app/index.html')
