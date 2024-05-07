from django.db import models


class MedCards(models.Model):
    patient = models.OneToOneField('auth_app.Patient', on_delete=models.CASCADE, verbose_name='ID пацієнта')
    doctor = models.ForeignKey('auth_app.Doctor', on_delete=models.SET_DEFAULT, default='Лікаря не назначено', verbose_name='ID лікаря')
    dispensary_group = models.BooleanField(verbose_name='Диспансерна група')
    registration_date = models.DateField(verbose_name='Поставлено на облік')
    deregistration_date = models.DateField(blank=True, null=True, verbose_name='Знято з обліку')
    class Meta:
        db_table = 'MedCards'
        verbose_name = 'Медичну карту'
        verbose_name_plural = 'Медичні картки'
    def __str__(self):
        return f"{self.id}."
    def display_id(self):
        return f'{self.id:05}'



class SignalMarks(models.Model):
    name = models.CharField(max_length=50, unique=True,verbose_name='Сигнальна позначка')
    id_medcard = models.ManyToManyField('MedCards', through='IndividualMarks')
    class Meta:
        db_table = 'SignalMarks'
        verbose_name = 'Сигнальну позначку'
        verbose_name_plural = 'Сигнальні позначки'
    def __str__(self):
        return f"{self.id}.{self.name}"    



class IndividualMarks(models.Model):
    value = models.CharField(max_length=100, verbose_name='Значення')
    medcard = models.ForeignKey('MedCards', on_delete=models.CASCADE, verbose_name='Номер медичної карти')
    signal_mark = models.ForeignKey('SignalMarks', on_delete=models.CASCADE, verbose_name='Cигнальна позначка')

    class Meta:
        db_table = 'IndividualMarks'
        verbose_name = 'Індивідуальну позначку'
        verbose_name_plural = 'Індивідуальні позначки'
    def __str__(self):
        return f"{self.id}.{self.medcard} має позначку {self.name}"  
        


class Vaccination(models.Model):
    name = models.CharField (max_length=100, unique=True, verbose_name='Найменування щеплення')
    dose_number = models.PositiveSmallIntegerField(verbose_name='Кількість доз')
    age = models.PositiveSmallIntegerField(verbose_name='Вік для щеплення')
    active_substance = models.CharField(max_length=100, blank=True, null=True, verbose_name='Активна речовина')
    METHOD = [
        ("Внутрішньом'язова", "Внутрішньом'язова ін'єкція"),
        ("Підшкірна", "Підшкірна ін'єкція"),
        ("Внутрішньошкірна", "Внутрішньошкірна ін'єкція"),
        ("Перорально", "Перорально(через рот)")
    ]
    input_method = models.CharField(choices=METHOD, max_length=30,  blank=True, null=True, verbose_name='Cпосіб введення')
    id_medcard = models.ManyToManyField('MedCards', through='CardVaccine')
    class Meta:
        db_table = 'Vaccination'
        verbose_name = 'Щеплень'
        verbose_name_plural = 'Щеплення'
    def __str__(self):
        return f"{self.id}.{self.name}" 
    


class CardVaccine(models.Model):
    date_vaccine = models.DateField(verbose_name='Дата вакцинації')
    REACTION = [
        ('Місцева', 'Місцева'),
        ('Загальна', 'Загальна')
    ]
    reaction = models.CharField(choices=REACTION, max_length=20, verbose_name='Реакція на щеплення')
    contraindication  = models.CharField(max_length=300, verbose_name='Протипоказання')
    medcard = models.ForeignKey('MedCards', on_delete=models.CASCADE, verbose_name='Номер медичної карти')
    vaccination = models.ForeignKey('Vaccination', on_delete=models.CASCADE, verbose_name='Найменування щеплення')
    class Meta:
        db_table = 'CardVaccine'
        verbose_name = 'Щеплень в медичній карті'
        verbose_name_plural = 'Щеплення в картці'
    def __str__(self):
        return f"{self.id}.{self.medcard} - {self.date_vaccine}"         



class DoctorExamination(models.Model):
    reason_for_contacting = models.CharField(max_length=100, verbose_name='Причина звернення')
    cabinet = models.CharField(max_length=10, blank=True, null=True, verbose_name='Кабінет')
    date_visit = models.DateField(verbose_name='Дата прийому')
    report = models.CharField(max_length=1000, verbose_name='Висновки')
    doctor = models.ForeignKey('auth_app.Doctor', on_delete=models.DO_NOTHING, verbose_name='Особистий номер лікаря')
    medcard = models.ForeignKey('MedCards', on_delete=models.CASCADE, verbose_name='Номер медичної карти')
    class Meta:
        db_table = 'DoctorExamination'
        verbose_name = 'Запис про огляд'
        verbose_name_plural = 'Записи про огляд'
    def __str__(self):
        return f"{self.id}.{self.medcard} - {self.reason_for_contacting}"
        
