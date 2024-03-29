# Generated by Django 4.0 on 2022-07-29 11:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_order_estimated_duration_of_transit'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='commodity',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='darsher',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='darshercompany',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='stores',
            name='bio',
            field=models.CharField(max_length=1000, null=True, verbose_name='bio'),
        ),
        migrations.AddField(
            model_name='stores',
            name='closing_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='closing_time'),
        ),
        migrations.AddField(
            model_name='stores',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='stores',
            name='opening_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='opening_time'),
        ),
        migrations.AddField(
            model_name='stores',
            name='phone_number',
            field=models.CharField(max_length=200, null=True, verbose_name='phone_number'),
        ),
        migrations.AddField(
            model_name='stores',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='top_city',
            field=models.BooleanField(default=False, verbose_name='top_city'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='stores',
            name='favorite',
            field=models.BooleanField(default=False, verbose_name='favourite'),
        ),
        migrations.AlterField(
            model_name='stores',
            name='status',
            field=models.CharField(choices=[('Delivering now!', 'Active'), ('Coming soon', 'Comingsoon'), ('Delivering in 10 min', 'Soon'), ('Not active', 'Inactive')], default='Not active', max_length=200, verbose_name='status'),
        ),
    ]
