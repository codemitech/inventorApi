# Generated by Django 4.0.4 on 2022-05-07 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0035_remove_investment_invester_investment_investor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investment',
            old_name='investor',
            new_name='user',
        ),
    ]