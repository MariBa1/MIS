# Generated by Django 4.2.11 on 2024-05-07 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_familydoctor_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='familydoctor',
            options={'verbose_name': 'Cімейного лікаря', 'verbose_name_plural': 'Сімейні лікарі'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Фото'),
        ),
    ]