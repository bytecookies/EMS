# Generated by Django 3.2.16 on 2023-01-04 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_exhibitorbrandorcompanylogo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibitor',
            name='upload_company_or_brand_logo',
        ),
    ]
