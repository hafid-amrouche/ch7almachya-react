# Generated by Django 4.2.7 on 2024-03-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0030_alter_contactus_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='reply',
            field=models.TextField(null=True),
        ),
    ]
