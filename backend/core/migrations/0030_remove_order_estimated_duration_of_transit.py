# Generated by Django 4.0 on 2022-07-29 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_order_estimated_duration_of_transit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='estimated_duration_of_transit',
        ),
    ]