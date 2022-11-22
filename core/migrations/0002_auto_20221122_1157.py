# Generated by Django 3.2.16 on 2022-11-22 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendercontact',
            old_name='de',
            new_name='department',
        ),
        migrations.AddField(
            model_name='exhibitor',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='utility.department'),
        ),
        migrations.AddField(
            model_name='exhibitor',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='utility.designation'),
        ),
        migrations.AddField(
            model_name='exhibitor',
            name='senior_department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='senior_department', to='utility.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exhibitor',
            name='senior_designation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='senior_designation', to='utility.designation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendercontact',
            name='designation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='utility.designation'),
            preserve_default=False,
        ),
    ]