# Generated by Django 4.0.4 on 2022-05-08 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0040_rename_facabook_url_investor_facebook_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventor',
            old_name='facabook_url',
            new_name='facebook_url',
        ),
    ]
