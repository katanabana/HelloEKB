# Generated by Django 4.2.4 on 2023-08-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, choices=[['Sport', 'Спорт'], ['Culture', 'Культура'], ['Education', 'Образование'], ['Hobby', 'Хобби']], max_length=255, null=True, verbose_name='Category'),
        ),
    ]
