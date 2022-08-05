# Generated by Django 4.0 on 2022-07-29 15:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_order_time_arrived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='reviews',
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('review', models.TextField(max_length=1000, verbose_name='reviews')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reviewer', to='core.customuser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='reviews',
            field=models.ManyToManyField(related_name='reviewss', to='core.Reviews'),
        ),
    ]