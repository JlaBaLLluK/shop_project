# Generated by Django 4.2.5 on 2023-10-12 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale_advertisement', '0003_saleadvertisement_views_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saleadvertisement',
            name='currency',
        ),
    ]
