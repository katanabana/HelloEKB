# Generated by Django 4.2.4 on 2023-08-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Description'),
        ),
    ]
