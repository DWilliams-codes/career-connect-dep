# Generated by Django 4.2.3 on 2023-08-13 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='education_app.education')),
            ],
        ),
    ]