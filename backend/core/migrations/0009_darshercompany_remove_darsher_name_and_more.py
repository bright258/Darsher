# Generated by Django 4.0 on 2022-07-22 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_stores_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DarsherCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='darsher',
            name='name',
        ),
        migrations.AddField(
            model_name='consumer',
            name='phone_number',
            field=models.CharField(max_length=200, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='darsher',
            name='darsher_order_status',
            field=models.CharField(choices=[('ACCEPT', 'Accept'), ('REJECT', 'Reject')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='darsher',
            name='first_name',
            field=models.CharField(max_length=200, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='darsher',
            name='last_name',
            field=models.CharField(max_length=200, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='darsher',
            name='location',
            field=models.CharField(max_length=200, null=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='darsher',
            name='status',
            field=models.CharField(choices=[('Curretly delievering an order', 'Delivering'), ('Free', 'Not Delivering'), ('inactive', 'Inactive')], max_length=200, null=True, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='darsher',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transport_company', to='core.darshercompany'),
        ),
    ]