# Generated by Django 4.2.11 on 2024-05-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_alter_familydoctor_options_alter_customuser_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(blank=True, verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, choices=[('Ч', 'Чоловік'), ('Ж', 'Жінка')], max_length=1, verbose_name='Cтать'),
        ),
    ]