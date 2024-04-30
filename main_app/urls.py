from django.urls import path

from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('',views.index, name='index'),  ## cилка на views
    path('about/',views.about, name='about'),  ## cилка на views
    path('contacts/',views.contact, name='contact'),  ## cилка на views

]