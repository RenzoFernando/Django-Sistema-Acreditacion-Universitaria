# Generated by Django 5.1.7 on 2025-05-26 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assignments', '0001_initial'),
        ('factorManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factorassignment',
            name='factor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factor_assignments_to_users', to='factorManager.factor'),
        ),
    ]
