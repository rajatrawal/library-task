# Generated by Django 5.0.1 on 2024-02-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_author_password_author_username_alter_author_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/cover/'),
        ),
    ]
