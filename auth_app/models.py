from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.validators import UnicodeUsernameValidator


class Address(models.Model):
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name= 'Місто')
    village = models.CharField(max_length=50, blank=True, null=True, verbose_name= 'Населений пункт')
    street = models.CharField(max_length=50, blank=True, null=True, verbose_name= 'Вулиця')
    bloc = models.CharField(max_length=50, blank=True, null=True, verbose_name= 'Блок')
    apartment = models.IntegerField(blank=True, null=True, verbose_name= 'Квартира')
    
    class Meta:
        db_table = 'Address'
        verbose_name = 'Адресу'
        verbose_name_plural = 'Адреси'


    def __str__(self):
        return self.city, self.street 

class CustomUser(AbstractUser): 

    img = models.ImageField(upload_to='media/%Y/%m', blank=True, null=True, verbose_name='Фото')
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name= 'По-батькові')
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name= 'Номер телефону')
    
    class Meta:
        db_table = 'Users'
        verbose_name = 'Користувача'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.username 

class Doctor(models.Model):
    tab_nomer = models.CharField(max_length=20, primary_key=True)
    user = models.OneToOneField("auth_app.CustomUser", verbose_name="ID користувача", on_delete=models.CASCADE)
    stazh = models.CharField(max_length=30, blank=True, default="Не вказано",verbose_name='Cтаж')
    specialization = models.CharField(max_length=100, blank=True, default="Не вказано",verbose_name='Спеціалізація')
    #slug = models.SlugField(),
    Umovy_pryyomu = models.CharField(max_length=250, blank=True, default="Не вказано",verbose_name='Умови прийому')
    
    class Meta:
        db_table = 'Doctor'
        verbose_name = 'Лікаря'
        verbose_name_plural = 'Лікарі'

    def __str__(self):
        return self.tab_nomer, #self.slug

class Patient(models.Model):
    SEX = [
        ('Ч','Чоловік'),
        ('Ж','Жінка'),]
    sex = models.CharField(max_length=1, choices=SEX, verbose_name='Cтать',default='Ч')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата народження')
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.SET_NULL)
    #slug = models.SlugField(unique=True, editable=False)
    
    class Meta:
        db_table = 'Patient'
        verbose_name = 'Пацієнта'
        verbose_name_plural = 'Пацієнти'

    def __str__(self):
        return self.date_of_birth 


