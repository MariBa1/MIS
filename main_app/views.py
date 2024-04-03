from django.shortcuts import render

def index(request):
    return render(request, 'main_app/index.html')

def about(request):
    return render(request, 'main_app/about.html')

def contact(request):
    return render(request, 'main_app/contacts.html')