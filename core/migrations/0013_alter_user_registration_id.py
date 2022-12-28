# Generated by Django 3.2.16 on 2022-12-12 09:43

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_user_registration_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration_id',
            field=models.CharField(default=core.models.unique_id, max_length=12, unique=True),
        ),
    ]