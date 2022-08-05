# Generated by Django 4.0 on 2022-07-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_stores_closing_time_alter_stores_opening_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='currency',
            field=models.CharField(choices=[('NGN', 'Ngn'), ('USD', 'Usd'), ('CND', 'Cnd')], default='NGN', max_length=3, verbose_name='currency'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Sold out', 'Sold Out')], default='Available', max_length=10, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='darshercompany',
            name='bio',
            field=models.TextField(max_length=1000, null=True, verbose_name='bio'),
        ),
        migrations.AddField(
            model_name='darshercompany',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='darshercompany',
            name='locations',
            field=models.ManyToManyField(related_name='locations', to='core.Location'),
        ),
        migrations.AddField(
            model_name='darshercompany',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, verbose_name='phone_number'),
        ),
        migrations.AddField(
            model_name='darshercompany',
            name='website_url',
            field=models.URLField(null=True, verbose_name='website'),
        ),
        migrations.AddField(
            model_name='stores',
            name='website_url',
            field=models.URLField(null=True, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='description',
            field=models.TextField(max_length=500, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='image',
            field=models.ImageField(upload_to='then', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='darshercompany',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='stores',
            name='bio',
            field=models.TextField(max_length=1000, null=True, verbose_name='bio'),
        ),
        migrations.AlterField(
            model_name='stores',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, verbose_name='phone_number'),
        ),
    ]