# Generated by Django 3.2 on 2021-12-11 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('recipes', '0002_auto_20211211_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdventCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advent_calendar_number', models.CharField(editable=False, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('advent_calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advent_calendar_days', to='advent_calendar.adventcalendar')),
                ('days_recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='adventcalendar',
            name='days',
            field=models.ManyToManyField(to='advent_calendar.Day'),
        ),
        migrations.AddField(
            model_name='adventcalendar',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_advent_calendar', to='profiles.userprofile'),
        ),
    ]
