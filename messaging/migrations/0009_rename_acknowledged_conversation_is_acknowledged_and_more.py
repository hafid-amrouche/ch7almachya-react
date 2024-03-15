# Generated by Django 4.2.7 on 2024-01-29 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0008_rename_is_acknowledged_conversation_acknowledged_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='acknowledged',
            new_name='is_acknowledged',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='seen_by_receiver',
            new_name='is_seen_by_receiver',
        ),
    ]
