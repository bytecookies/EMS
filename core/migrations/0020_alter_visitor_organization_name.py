# Generated by Django 3.2.16 on 2022-12-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_visitor_cc_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='organization_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
