# Generated by Django 4.0 on 2022-07-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_darsher_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darsher',
            name='darsher_order_status',
            field=models.CharField(blank=True, choices=[('ACCEPT', 'Accept'), ('REJECT', 'Reject')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='darsher',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='darsher',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='last_name'),
        ),
    ]