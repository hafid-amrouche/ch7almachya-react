# Generated by Django 4.2.7 on 2024-02-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_profile_email_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('times', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]