from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ValidationError
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField



# class Address(models.Model):
#     city = models.CharField(max_length=50, blank=True, null=True, verbose_name= 'Місто')
#     village = models.CharField(max_length=50, blank=True, null=True, verbose_name= 'Населений пункт')
#     street = models.CharField(max_length=50, blank=True, null=True, verbose_name= 'Вулиця')
#     house = models.PositiveIntegerField(blank=True, null=True, verbose_name= 'Будинок', validators=[MinValueValidator(1)])
#     apartment = models.PositiveIntegerField(blank=True, null=True, verbose_name= 'Квартира', validators=[MinValueValidator(1)])
#     class Meta:
#         db_table = 'Address'
#         verbose_name = 'Адресу'
#         verbose_name_plural = 'Адреси'
#     def __str__(self):
#         return f"{self.id}. {self.city}, {self.street}"
#     def clean(self):
#         existing_address = Address.objects.filter(
#             city=self.city,
#             village=self.village,
#             street=self.street,
#             house=self.house,
#             apartment=self.apartment
#         ).exists()
#         if existing_address:
#             raise ValidationError("Адреса вже існує.")
        
#     def save(self, *args, **kwargs):
#         if not(self.city or self.village or self.street or self.house or self.apartment):
#             return
#         super().save(*args, **kwargs)



class CustomUser(AbstractUser): 
    img = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name='Фото')
    email = models.EmailField(unique=True, verbose_name= 'Email')
    first_name = models.CharField(max_length=100, verbose_name= 'Iмя')
    last_name = models.CharField(max_length=100, verbose_name= 'Призвіще')
    patronymic = models.CharField(max_length=100, blank=True, null=True, verbose_name= 'По-батькові')
    phone_number = PhoneNumberField(unique=True, verbose_name= 'Номер телефону')
    class Meta:
        db_table = 'Users'
        verbose_name = 'Користувача'
        verbose_name_plural = 'Користувачі'
    def __str__(self):
        return f"{self.id}. Логін: {self.username}"



class Doctor(models.Model):
    tab_nomer = models.CharField(max_length=20, primary_key=True,verbose_name="Табельний номер")
    user = models.OneToOneField("auth_app.CustomUser", verbose_name="ID користувача", on_delete=models.CASCADE)
    stazh = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cтаж')
    specialization = models.CharField(max_length=100,verbose_name='Спеціалізація')
    #slug = models.SlugField(),
    Umovy_pryyomu = models.CharField(max_length=250, blank=True, null=True, verbose_name='Умови прийому')    
    class Meta:
        db_table = 'Doctor'
        verbose_name = 'Лікаря'
        verbose_name_plural = 'Лікарі'
    def __str__(self):
        return self.tab_nomer #self.slug



class Patient(models.Model):
    user = models.OneToOneField("auth_app.CustomUser", verbose_name="ID користувача", on_delete=models.CASCADE)
    SEX = [
        ('Ч','Чоловік'),
        ('Ж','Жінка'),]
    sex = models.CharField(blank=True, null=True, max_length=1, choices=SEX, verbose_name='Cтать')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата народження')
    # address = models.ForeignKey("auth_app.Address", blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Адреса')
    id_doctor = models.ManyToManyField("auth_app.Doctor", 
                                        through='FamilyDoctor')
    #slug = models.SlugField(unique=True, editable=False)    
    class Meta:
        db_table = 'Patient'
        verbose_name = 'Пацієнта'
        verbose_name_plural = 'Пацієнти'
    def __str__(self):
        return f"{self.user}"


class FamilyDoctor(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пацієнт')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,verbose_name='Лікар')

    class Meta:
      db_table = 'FamilyDoctor'
      verbose_name = 'Сімейного лікаря'
      verbose_name_plural = 'Сімейні лікарі'
      unique_together = ('patient', 'doctor')

    def __str__(self):
      return f"{self.doctor} - {self.patient}"

