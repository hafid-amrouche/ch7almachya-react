# Generated by Django 4.2.7 on 2024-03-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0036_alter_report_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]