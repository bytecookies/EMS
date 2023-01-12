# Generated by Django 3.2.16 on 2023-01-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_alter_meeting_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, unique=True, verbose_name='email or mobile'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]