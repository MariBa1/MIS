from django.shortcuts import render

def index(request):
    return render(request, 'cards_app/all_for_doc.html')

def profile_pat(request):
    return render(request, 'cards_app/prof_pat.html')

def profile_doc(request):
    return render(request, 'cards_app/prof_doc.html')
