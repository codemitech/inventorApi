# Generated by Django 4.0.4 on 2022-05-03 18:57

from django.db import migrations, models
import django.db.models.deletion
import inventor.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventor', '0028_alter_investment_invents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='Invents',
            field=models.OneToOneField(blank=True, default=inventor.models.inventions, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventor.inventions'),
        ),
    ]