# Generated by Django 4.0 on 2022-07-19 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_commodity_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FrequentlyAskedQuestions',
            new_name='FrequentlyAskedQuestion',
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Cities'},
        ),
    ]