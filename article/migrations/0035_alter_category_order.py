# Generated by Django 4.2.7 on 2024-02-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0034_alter_brand_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
