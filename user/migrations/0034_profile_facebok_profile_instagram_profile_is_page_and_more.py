# Generated by Django 4.2.7 on 2024-02-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_alter_profile_birth_day_public_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebok',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='other_socials',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='page_website',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tiktok',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
