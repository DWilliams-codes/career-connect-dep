# Generated by Django 4.2.3 on 2023-08-15 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant_app', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='favorites',
        ),
    ]
