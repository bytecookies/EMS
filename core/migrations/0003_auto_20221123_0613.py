# Generated by Django 3.2.16 on 2022-11-23 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221122_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitor',
            name='designation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='exhibitor',
            name='senior_designation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vendercontact',
            name='designation',
            field=models.CharField(max_length=200),
        ),
    ]
