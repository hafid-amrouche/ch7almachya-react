# Generated by Django 4.2.7 on 2024-01-26 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_rename_content_message_text_message_is_seen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='is_seen',
            new_name='is_seen_by_receiver',
        ),
    ]