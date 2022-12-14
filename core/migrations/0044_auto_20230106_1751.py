# Generated by Django 3.2.16 on 2023-01-06 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='exhibitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.exhibitor'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='visitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.visitor'),
        ),
    ]
