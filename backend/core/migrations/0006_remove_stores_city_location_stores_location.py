# Generated by Django 4.0 on 2022-07-19 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_frequentlyaskedquestions_frequentlyaskedquestion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stores',
            name='city',
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='core.city')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='stores',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='core.location'),
        ),
    ]