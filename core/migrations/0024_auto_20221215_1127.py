# Generated by Django 3.2.16 on 2022-12-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_user_registration_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='badge_company',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='visitor',
            name='badge_job_title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='visitor',
            name='badge_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
