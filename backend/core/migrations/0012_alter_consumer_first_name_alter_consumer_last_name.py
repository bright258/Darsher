# Generated by Django 4.0 on 2022-07-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_consumer_first_name_alter_consumer_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='last_name'),
        ),
    ]