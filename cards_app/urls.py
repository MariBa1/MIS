from django.urls import path

from cards_app import views

app_name = 'cards_app'

urlpatterns = [

    path('all_cards/',views.all_cards, name='all_cards'),

]