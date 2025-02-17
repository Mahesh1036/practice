# Generated by Django 5.1.2 on 2024-10-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('height', models.FloatField(help_text='Height in cm')),
                ('weight', models.FloatField(help_text='Weight in kg')),
                ('activity_level', models.CharField(choices=[('sedentary', 'Sedentary: little or no exercise'), ('light', 'Light: exercise 1-3 times/week'), ('moderate', 'Moderate: exercise 4-5 times/week'), ('active', 'Active: daily exercise or intense exercise 3-4 times/week'), ('very_active', 'Very Active: intense exercise 6-7 times/week')], max_length=20)),
            ],
        ),
    ]
