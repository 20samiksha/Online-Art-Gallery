# Generated by Django 3.0 on 2020-11-22 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0006_exhibtion_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exhibtion',
            old_name='exhibtion_day',
            new_name='exhibition_day',
        ),
        migrations.RenameField(
            model_name='exhibtion',
            old_name='exhibtion_location',
            new_name='exhibition_location',
        ),
    ]
