# Generated by Django 4.2.3 on 2023-08-13 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_posting_app', '0002_initial'),
        ('applicant_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applicant',
            name='favorites',
            field=models.ManyToManyField(default=None, related_name='applicants', to='job_posting_app.job_posting'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='skills',
            field=models.ManyToManyField(default=None, related_name='applicants', to='skills_app.skill'),
        ),
    ]