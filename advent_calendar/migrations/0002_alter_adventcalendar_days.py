# Generated by Django 3.2 on 2021-12-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advent_calendar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventcalendar',
            name='days',
            field=models.ManyToManyField(blank=True, to='advent_calendar.Day'),
        ),
    ]
