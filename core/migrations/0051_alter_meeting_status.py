# Generated by Django 3.2.16 on 2023-01-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_alter_eventagenda_speaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
