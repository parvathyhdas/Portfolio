# Generated by Django 5.0.1 on 2024-01-12 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdb',
            old_name='Subject',
            new_name='Message',
        ),
    ]