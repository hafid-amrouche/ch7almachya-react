# Generated by Django 4.2.7 on 2024-03-03 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0038_brand_name_ar_brand_name_en_brand_name_fr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='name_fr',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_fr',
        ),
        migrations.RemoveField(
            model_name='color',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='color',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='color',
            name='name_fr',
        ),
        migrations.RemoveField(
            model_name='document',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='document',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='document',
            name='name_fr',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='fuel',
            name='name_fr',
        ),
        migrations.RemoveField(
            model_name='gearbox',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='gearbox',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='gearbox',
            name='name_fr',
        ),
        migrations.RemoveField(
            model_name='option',
            name='name_ar',
        ),
        migrations.RemoveField(
            model_name='option',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='option',
            name='name_fr',
        ),
    ]
