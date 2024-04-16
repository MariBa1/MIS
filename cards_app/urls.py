from django.urls import path

from cards_app import views

app_name = 'cards_app'

urlpatterns = [
    path('all/',views.index, name='index'),  ## cилка на views

]