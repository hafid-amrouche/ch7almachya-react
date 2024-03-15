# Generated by Django 4.2.7 on 2024-01-07 15:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0010_article_savers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='savers',
            field=models.ManyToManyField(related_name='saved_aricles', to=settings.AUTH_USER_MODEL),
        ),
    ]