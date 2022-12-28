# Generated by Django 3.2.16 on 2022-12-28 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20221228_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='schedule_request_time',
            new_name='schedule_request_date',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='schedule_time',
        ),
        migrations.AddField(
            model_name='meeting',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='time_form',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='time_to',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myschedule',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myschedule',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='myschedule',
            name='time_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='myschedule',
            name='time_to',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
