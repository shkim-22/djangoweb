# Generated by Django 3.2.25 on 2024-09-09 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20240909_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='text',
            new_name='maintext',
        ),
    ]
