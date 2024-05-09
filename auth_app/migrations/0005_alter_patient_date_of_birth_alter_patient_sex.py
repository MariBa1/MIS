# Generated by Django 4.2.11 on 2024-05-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_alter_patient_date_of_birth_alter_patient_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, choices=[('Ч', 'Чоловік'), ('Ж', 'Жінка')], max_length=1, null=True, verbose_name='Cтать'),
        ),
    ]