from django.urls import path

from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('registration/',views.reg, name='registration'),
    path('logout/',views.logout, name='logout'),

    path('doctor1/',views.profile_doc, name='prof_doc'),
    path('doctor1/new_pass/',views.new_pass, name='new_pass'),

]