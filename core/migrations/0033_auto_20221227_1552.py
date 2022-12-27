# Generated by Django 3.2.16 on 2022-12-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20221223_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='myschedule',
            name='add_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='myschedule',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myschedule',
            name='sender_to_receiver_type',
            field=models.CharField(blank=True, choices=[('A-AL', 'A-AL'), ('V-E', 'V-E'), ('E-V', 'E-V')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='myschedule',
            name='time_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myschedule',
            name='time_to',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='personal_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='sender_type',
            field=models.CharField(choices=[('VISITOR', 'VISITOR'), ('EXHIBITOR', 'EXHIBITOR')], max_length=255),
        ),
    ]
