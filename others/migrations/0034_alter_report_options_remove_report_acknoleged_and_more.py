# Generated by Django 4.2.7 on 2024-03-28 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0033_remove_report_note_remove_report_reporter_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={},
        ),
        migrations.RemoveField(
            model_name='report',
            name='acknoleged',
        ),
        migrations.RemoveField(
            model_name='report',
            name='article',
        ),
        migrations.RemoveField(
            model_name='report',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='report',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='report',
            name='ruled_deleted',
        ),
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
    ]