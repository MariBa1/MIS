# Generated by Django 4.2.11 on 2024-05-17 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_alter_familydoctor_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familydoctor',
            name='group',
        ),
    ]