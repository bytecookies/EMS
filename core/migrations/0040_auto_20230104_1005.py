# Generated by Django 3.2.16 on 2023-01-04 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_exhibitor_sd_key_person_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='fascia_form_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exhibitor',
            name='showdirectory_form_status',
            field=models.BooleanField(default=False),
        ),
    ]
