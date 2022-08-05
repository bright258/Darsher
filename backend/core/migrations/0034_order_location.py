# Generated by Django 4.0 on 2022-08-02 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_alter_order_time_arrived'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='location',
            field=models.ManyToManyField(related_name='customer_location', to='core.Location'),
        ),
    ]