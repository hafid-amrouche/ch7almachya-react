# Generated by Django 4.2.7 on 2024-03-06 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0041_country_name_ar_country_name_en_country_name_fr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='order',
        ),
    ]
