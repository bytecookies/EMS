# Generated by Django 3.2.16 on 2022-12-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20221227_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='company_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
