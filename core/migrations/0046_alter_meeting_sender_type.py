# Generated by Django 3.2.16 on 2023-01-08 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20230109_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='sender_type',
            field=models.CharField(choices=[('---', '---'), ('VISITOR', 'VISITOR'), ('EXHIBITOR', 'EXHIBITOR')], max_length=255),
        ),
    ]