# Generated by Django 4.2.11 on 2024-05-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medcards',
            name='deregistration_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Знято з обліку'),
        ),
        migrations.AlterField(
            model_name='medcards',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Поставлено на облік'),
        ),
    ]
