# Generated by Django 3.2.16 on 2022-12-15 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20221215_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorIdPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('visitor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.visitor')),
            ],
        ),
    ]
