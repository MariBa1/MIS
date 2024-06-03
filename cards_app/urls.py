from django.urls import path

from cards_app import views

app_name = 'cards_app'

urlpatterns = [

    path('all-cards/',views.all_cards, name='all_cards'), # med-card/all-cards/
    path('<int:card_id>/',views.index, name='index'), # med-card/00005/
    path('vaccine/<int:card_id>/',views.vaccine, name='vaccine'), 
    # path('examination/<int:card_id>/',views.examination, name='examination'),

    path('card-profile/', views.card_profile, name='card_profile'), # med-card/card-profile/
    path('vaccine-profile/', views.vaccine_profile, name='vaccine_profile'), 
    # path('examination-profile/', views.examination_profile, name='examination_profile'),

    path('error/',views.not_card, name='error'), ##### med-card/error

    path('add-vaccine/<int:card_id>/', views.add_vaccine, name='add_vaccine'),
    path('delete-vaccine/<int:card_id>/', views.delete_vaccine, name='delete_vaccine'),

]