# Generated by Django 3.2.16 on 2023-01-08 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20230106_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='exhibitor',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='visitor',
        ),
        migrations.AddField(
            model_name='meeting',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meeting',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='core.user'),
            preserve_default=False,
        ),
    ]