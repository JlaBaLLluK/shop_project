# Generated by Django 4.2.5 on 2023-10-18 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourite_advertisements', '0002_remove_favouriteadvertisements_advertisements_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favouriteadvertisements',
            old_name='advertisements',
            new_name='advertisement',
        ),
    ]
