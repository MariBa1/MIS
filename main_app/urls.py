from django.urls import path
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('',views.index, name='index'),  ## 8000/
    path('contacts/',views.contact, name='contact'),  ## 8000/contacts
]