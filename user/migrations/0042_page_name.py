# Generated by Django 4.2.7 on 2024-02-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0041_alter_userextention_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
