# Generated by Django 4.2.7 on 2024-02-11 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0024_remove_article_main_image_mainimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainimage',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.image'),
        ),
    ]