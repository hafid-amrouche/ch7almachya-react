# Generated by Django 4.2.7 on 2024-02-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20240209_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersuggestion',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]
