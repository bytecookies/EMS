# Generated by Django 3.2.16 on 2022-12-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_user_registration_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='gender',
            field=models.CharField(choices=[('---', ''), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=49),
        ),
    ]