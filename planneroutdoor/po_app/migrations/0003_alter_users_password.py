# Generated by Django 5.1.1 on 2024-10-02 22:27

import django.contrib.auth.password_validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('po_app', '0002_alter_activities_options_alter_allergens_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=128, validators=[django.contrib.auth.password_validation.validate_password]),
        ),
    ]
