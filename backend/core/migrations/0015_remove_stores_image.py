# Generated by Django 4.0 on 2022-07-26 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_darsher_darsher_order_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stores',
            name='image',
        ),
    ]
