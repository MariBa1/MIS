from django.urls import path

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('registration/',views.reg, name='registration'),
    path('logout/',views.logout, name='logout'),  ## cилка на views

]