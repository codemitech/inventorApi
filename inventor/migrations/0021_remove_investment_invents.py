# Generated by Django 4.0.4 on 2022-05-03 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0020_rename_inventions_investment_invents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investment',
            name='Invents',
        ),
    ]
