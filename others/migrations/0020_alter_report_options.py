# Generated by Django 4.2.7 on 2024-03-24 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0019_contactus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-created_at']},
        ),
    ]
