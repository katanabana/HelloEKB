# Generated by Django 4.2.4 on 2023-08-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, choices=[['Sport', 'Sport'], ['Culture', 'Culture'], ['Education', 'Education'], ['Hobby', 'Hobby']], max_length=255, null=True, verbose_name='Category'),
        ),
    ]
