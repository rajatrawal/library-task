# Generated by Django 5.0.1 on 2024-01-31 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_author_auth_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='city_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.city'),
        ),
    ]