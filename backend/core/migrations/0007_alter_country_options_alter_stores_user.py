# Generated by Django 4.0 on 2022-07-19 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_stores_city_location_stores_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Countries'},
        ),
        migrations.AlterField(
            model_name='stores',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stores', to='core.customuser'),
        ),
    ]
