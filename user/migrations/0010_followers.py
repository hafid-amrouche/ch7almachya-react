# Generated by Django 4.2.7 on 2024-01-05 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0009_profile_credibility_profile_rank_profile_scoore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers_list', models.ManyToManyField(related_name='followers_list', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
