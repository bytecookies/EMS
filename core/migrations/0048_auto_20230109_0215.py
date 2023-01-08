# Generated by Django 3.2.16 on 2023-01-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20230109_0202'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time_form', models.TimeField(blank=True, null=True)),
                ('time_to', models.TimeField(blank=True, null=True)),
                ('add_date_time', models.DateTimeField(auto_now=True, verbose_name='Schedule Request Time')),
            ],
        ),
        migrations.AddField(
            model_name='myschedule',
            name='event_agendas',
            field=models.ManyToManyField(blank=True, to='core.EventAgenda'),
        ),
    ]
