# Generated by Django 4.0 on 2022-07-29 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_commodity_currency_commodity_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='darsher',
            name='darsher_order_status',
        ),
        migrations.AddField(
            model_name='consumer',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='address'),
        ),
        migrations.AddField(
            model_name='darsher',
            name='orders',
            field=models.ManyToManyField(related_name='orders', to='core.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='darsher_order_status',
            field=models.CharField(blank=True, choices=[('ACCEPT', 'Accept'), ('REJECT', 'Reject')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='darsher',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='darsher_location', to='core.location'),
        ),
        migrations.AlterField(
            model_name='darsher',
            name='status',
            field=models.CharField(choices=[('Curretly delievering an order', 'Delivering'), ('Free', 'Not Delivering'), ('inactive', 'Inactive')], default='inactive', max_length=200, null=True, verbose_name='status'),
        ),
    ]