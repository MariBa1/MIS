from django.urls import path

from cards_app import views

app_name = 'cards_app'

urlpatterns = [
    path('all/',views.index, name='index'),  ## cилка на views
    path('patient/',views.profile_pat, name='prof_pat'),
    path('doctor/',views.profile_doc, name='prof_doc'),

]