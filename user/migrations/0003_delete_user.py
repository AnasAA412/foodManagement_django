# Generated by Django 4.1.5 on 2023-02-21 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_name_user_firstname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
