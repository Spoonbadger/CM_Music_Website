# Generated by Django 5.0.6 on 2024-09-19 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm_music', '0002_contact_delete_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactMessage',
        ),
    ]
